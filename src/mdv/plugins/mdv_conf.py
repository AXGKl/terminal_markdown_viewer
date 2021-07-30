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

validators = []
plugin = 'conf'
cli_actions = tools.cli_actions


# ------------------------------------------------------------------------------- tools
def loads(v):
    import json as j

    return j.loads(v)


def cast(k, v, into):
    """env, cli value into correct type, according to file conf"""
    if k not in into:
        return v
    dflt = into[k]
    if isinstance(dflt, (tuple, list)):
        return loads(v)
    elif isinstance(dflt, dict):
        dflt.update(loads(v))
        return dflt
    elif dflt == None:
        return v
    return type(dflt)(v)


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
    e = os.environ
    s = len(pref)
    l = [k[s:] for k in e if k.startswith(pref)]
    for k in l:
        into[k[s:]] = cast(k, e[pref + k], into)


actions = lambda: tools.FileConfig[0].Plugins.Actions

not_conf_args = {}


def from_cli(into, argv):
    args = argv[1:]
    while args:
        a = args.pop(0)
        if a[:2] == '--':
            a = a[2:]
            if '=' in a:
                a, v = a.split('=', 1)
            else:
                v = args.pop(0) if args else 'True'
            a = a.replace('-', '_')
            b = cast(a, v, into)
            if not a in into:
                not_conf_args[a] = b
            into[a] = b
            if b in (True, False):
                args.insert(0, v)
        elif a == '-':
            into['src'] = sys.stdin.read()
        elif into.get(a) and getattr(actions(), a, None):
            cli_actions.append(a)
        elif os.path.exists(a):
            into['src'] = tools.read_file(a)
        else:
            into['src'] = a


def validate(into):
    for v in validators:
        k = v[0]
        if not into[k] in v[1]:
            tools.die('Validation error', key=k, req=v[1], given=into[k])


# ------------------------------------------------------------------------ API CONTRACT


def configure(argv=None):
    """
    Populating a dict with all config values, enriched with env and cli
    """
    conf = tools.plugins.config  # user's or ours
    C = tools.C
    from_file(C, conf)
    p = C.get('environ_prefix')
    if p:
        from_env(C, p)
    if argv:
        from_cli(C, argv)
    validate(C)  # there is an option list feature
    w = C['width']
    h = C['height']
    if w == 0 or h == 0:
        wt, ht = tools.true_terminal_size(C)
        C['width'] = w or wt
        C['height'] = h or ht
    if '-h' in argv or '--help' in argv:
        cli_actions.insert(0, 'help')
    else:
        if not cli_actions:
            cli_actions.append('view')


def simple_cast(v):
    # good enough for now, if you need more overload with your plugin:
    try:
        return float(v)
    except:
        try:
            return int(v)
        except:
            return v


def run():
    for a in cli_actions:
        try:
            p = getattr(tools.plugins, a)
        except ModuleNotFoundError:
            tools.die('Is no plugin', argument=a)
        run = getattr(p, 'run', None)
        if run == None:
            tools.die('Is no valid action', action=a)
        # func args not in config?
        fa = not_conf_args
        if fa:

            for k, v in fa.items():
                fa[k] = simple_cast(v)
        try:
            run(**fa)
        except TypeError:
            # check only after miss, not always, startup speed.
            from inspect import getargspec as ga

            s = ga(run)
            miss = [k for k in fa if not k in s.args]
            if not s.keywords and miss:
                tools.die('Not understood', arg=','.join(miss))
            raise
