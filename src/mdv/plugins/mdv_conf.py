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
from mdv.globals import err, CLI, ActionResults
from mdv.plugs import plugins

validators = []
plugin = 'conf'


# ----------------------------------------------------------------------------- api dev
def from_file(into, c):
    """Creating a flat dict from our config.py when not user's present"""
    l = [k for k in dir(c) if not k[0] == '_']
    for k in l:
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


actions = lambda: tools.FileConfig[0].Plugins.Actions


def validate(into):
    for v in validators:
        k = v[0]
        if not into[k] in v[1]:
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
    actions = CLI.actions
    not_conf_args = CLI.not_conf_args
    # into will later update tools.C dict (in conf, def configure)
    args = argv[1:]
    while args:
        a = args.pop(0)
        if a[:2] == '--':
            a = a[2:]
            if '=' in a:
                a, v = a.split('=', 1)
            else:
                v = args.pop(0) if args else 'true'
            a = a.replace('-', '_')
            if not a in into:
                b = simple_cast(v)
                not_conf_args[a] = b
            else:
                b = cast(a, v, into)
            into[a] = b
            if b is True or b is False:
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
            actions.append(a)
    not_conf_args.pop('config_dir', 0)
    not_conf_args.pop('src', 0)


# :docs:argvparsing


# ------------------------------------------------------------------------ API CONTRACT


def configure(argv=None):
    """
    Populating a dict with all config values, enriched with env and cli
    """
    conf = plugins.config  # user's or ours
    C = tools.C
    actions = tools.CLI.actions
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
    if '-h' in argv or '--help' in argv:
        actions.insert(0, 'help')
    else:
        if not actions:
            actions.append('view')
    if getattr(conf.Plugins, 'log', None):
        # imports:
        plugins.log


def simple_cast(v):
    # good enough for now, if you need more overload with your plugin:
    try:
        return float(v)
    except:
        try:
            return int(v)
        except:
            return v


from inspect import getargspec


# :docs:conf_run_function
def run():
    actions = tools.CLI.actions
    not_conf_args = tools.CLI.not_conf_args
    C = tools.C
    for a in actions:
        try:
            p = getattr(plugins, a)
        except ModuleNotFoundError:
            return tools.die(err.is_no_plugin, argument=a)
        run = getattr(p, 'run', None)
        if run == None:
            return tools.die(err.is_no_valid_action, action=a)
        # func args not in config? Potentially typos:
        # we raise on those, if the sig has no kw args, else we pass them into run:
        fa = not_conf_args
        if fa:
            for k, v in fa.items():
                fa[k] = simple_cast(v)
        s = getargspec(run)
        kw = {}
        for a in s.args:
            v = fa.pop(a, C.get(a))
            if v is not None:
                kw[a] = v
        if s.keywords:
            kw.update(fa)
        else:
            if fa:
                tools.die(err.unknown_parameters, unknown=', '.join([k for k in fa]))
        ActionResults[a] = run(**kw)


# :docs:conf_run_function
