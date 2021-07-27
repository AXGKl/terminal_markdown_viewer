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
cli_actions = []


# class action:
#     kw = {}
#     conf = None

#     def prepare_actions():
#         # defaults and dependend actions
#         if not cli_actions:
#             cli_actions.add('view')
#         if 'html' in cli_actions and not 'view' in cli_actions:
#             cli_actions.append('view')

#     @classmethod
#     def view(action):
#         from mdv import markdownviewer

#         kw = action.kw
#         md = kw.get('md')
#         if md is None:
#             # e.g. mdv within a folder with a README.md -> render it w/o arg
#             fn = action.conf.get('filename')
#             if not fn or not os.path.exists(fn):
#                 tools.die('No markdown', hint='-h for help')
#             kw['md'] = tools.read_file(fn)
#         return markdownviewer.view(source=md, **action.kw)

#     @classmethod
#     def html(action):
#         breakpoint()  # FIXME BREAKPOINT
#         action['kw']
#         res = action.view


# ------------------------------------------------------------------------------- tools
def loads(v):
    j = tools.delayed_import('json')
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
            into[a] = b = cast(a, v, into)
            if b in (True, False):
                args.insert(0, v)
        elif a == '-':
            into['md'] = sys.stdin.read()
        elif into.get(a):
            cli_actions.append(a)
        elif os.path.exists(a):
            into['md'] = tools.read_file(a)
        else:
            into['md'] = a


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
    if not cli_actions:
        cli_actions.append('view')


def run():
    for a in cli_actions:
        try:
            p = getattr(tools.plugins, a)
        except ModuleNotFoundError as ex:
            tools.die('Is no plugin', argument=a)
        run = getattr(p, 'run', None)
        if run == None:
            tools.die('Is no valid action', action=a)
        run()
