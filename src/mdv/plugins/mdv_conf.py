"""_
# Contract

## Call Sequence
### configure(into[dict])

- Must populate the dict `into` with conf values, as from file, env, cli
- Must find the default action

### run
- runs the action

"""

import os
import sys

from mdv import tools
from mdv.globals import CLI, ActionResults, Actions, err  # , Finished
from mdv.plugs import plugins
from inspect import getfullargspec as getargspec

validators = []
plugin = 'conf'


# ----------------------------------------------------------------------------- api dev
def from_file(into, c):
    """Creating a flat dict from our config.py when not user's present"""
    keys = [k for k in dir(c) if not k[0] == '_']
    for k in keys:
        v = getattr(c, k)
        # nested class:
        if isinstance(v, type):
            from_file(into, c=v)
        else:
            if isinstance(v, tuple):
                validators.append((k, v[1]))
                v = v[0]
            into[k] = v


def from_env(into, pref):
    cast = tools.cast
    e = os.environ
    s = len(pref)
    l = [k[s:] for k in e if k.startswith(pref)]
    for k in l:
        into[k[s:]] = cast(k, e[pref + k], into)


def actions():
    return tools.FileConfig[0].Plugins.Actions


def validate(into):
    for v in validators:
        k = v[0]
        if callable(v[1]):
            into[k] = v[1](into[k])
        else:
            if into[k] not in v[1]:
                tools.die('Validation error', key=k, req=v[1], given=into[k])


# def add_cli(into):
#     kv = tools.CLI.kv
#     # remember the cli args not defined in config:
#     nc = tools.CLI.not_conf_args
#     # src and config_dir are never undefined, even if not in config:
#     ign = ['src', 'config_dir']
#     [nc.update({k: v}) for k, v in kv.items() if not k in into and not k in ign]
#     into.update(kv)


# :docs:argvparsing
def from_cli(into, argv):
    """Parsing argv, into a global dict (CLI)

    Have to do this early, before any conf, in order to get custom config_dir


    Mech:
    - When starting with "--" => it's a kv => value is after '=' or next arg, w/o an '='
    - values are obligatory
    - shortnames not yet supported
    - When a filename, the content is read into 'src' key
    - Otherwise it is considered an action
    """

    cast = tools.cast
    plugin_run_args = CLI.plugin_run_args
    # into will later update tools.C dict (in conf, def configure)
    args = argv[1:]
    while args:
        a = args.pop(0)
        if a in {'-h', '--help'}:
            Actions.insert(0, 'help')
            continue
        if a[:2] == '--':
            a = a[2:]
            if '=' in a:
                a, v = a.split('=', 1)
            else:
                if not args:
                    v = 'true'
                else:
                    v = args.pop(0)
                    if v.startswith('-'):
                        v = 'true'
            a = a.replace('-', '_')
            if a not in into:
                b = tools.autocast(v)
                plugin_run_args[a] = b
            else:
                b = cast(a, v, into)
            into[a] = b
            if args and b in {True, False}:
                args.insert(0, v)
        elif a == '-':
            into['src'] = sys.stdin.read()
        # elif into.get(a) and getattr(actions(), a, None):
        #     cli_actions.append(a)
        # elif os.path.exists(a):
        #     into['src'] = tools.read_file(a)
        # else:
        #     into['src'] = a
        elif os.path.exists(a):
            into['src'] = tools.read_file(a)
        else:
            # considered an action plugin name:
            Actions.append(a)

    plugin_run_args.pop('config_dir', 0)
    plugin_run_args.pop('src', 0)


# :docs:argvparsing


# ------------------------------------------------------------------------ API CONTRACT


def configure(argv=None):
    """
    Populating a dict with all config values, enriched with env and cli
    """
    conf = plugins.config  # user's or ours
    C = tools.C
    from_file(C, conf)
    p = C.get('environ_prefix')
    if p:
        from_env(C, p)
    if len(argv) > 1:
        from_cli(C, argv)
    validate(C)  # there is an option list feature
    w = C['width']
    h = C['height']
    if w == 0 or h == 0:
        wt, ht = tools.true_terminal_size(C)
        C['width'] = w or wt
        C['height'] = h or ht
    if not Actions:
        Actions.append('view')
    if getattr(conf.Plugins, 'log', None):
        # import the log:
        plugins.log  # noqa: B018


# :docs:conf_run_function
def run():
    plugin_run_args = CLI.plugin_run_args
    C = tools.C
    last_res = None
    while Actions:
        a = Actions.pop(0)
        try:
            p = getattr(plugins, a)
        except ModuleNotFoundError:
            return tools.die(err.is_no_plugin, argument=a)
        run = getattr(p, 'run', None)
        if run is None:
            return tools.die(err.is_no_valid_action, action=a)
        # func args not in config? Potentially typos:
        # we raise on those, if the sig has no kw args, else we pass them into run:
        fa = plugin_run_args
        if fa:
            for k, v in fa.items():
                fa[k] = tools.autocast(v)
        s = getargspec(run)
        kw = {}
        for a in s.args:
            v = fa.pop(a, C.get(a))
            if v is not None:
                kw[a] = v
        # if s.keywords:
        if s.varkw:
            kw.update(fa)
        else:
            if fa:
                tools.die(err.unknown_parameters, unknown=', '.join([k for k in fa]))
        ActionResults[a] = last_res = run(**kw)

    return last_res


# :docs:conf_run_function
