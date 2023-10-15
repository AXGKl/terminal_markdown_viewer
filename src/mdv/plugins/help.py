import sys

from mdv import tools
from mdv.plugs import plugins
from mdv.globals import CLI

acts = []


def show(c, r, p, n):
    r.append(p + ' ' + n)
    sub = []
    for k in sorted(dir(c)):
        if k[0] == '_':
            continue
        v = getattr(c, k)
        if isinstance(v, type):
            sub.append([k, v])
            if k == 'Actions':
                acts.append([k, v])
        else:
            r.append('- %s: %s' % (k, str(v)))

    for k, v in sub:
        show(v, r, p + '#', k)
        continue
    if p == '#':

        for k, v in acts:
            show(v, r, p + '#', k)
            continue


def run():
    """TODO: print this markdown rendered by mdv2"""
    h = False
    conf_mod = plugins.config
    p = '#'
    r = []
    res = []
    add = res.append
    add('\nParameters:\n')
    show(conf_mod, r, p, 'mdv2')
    add('\n'.join(r))
    add('\nActions:\n')
    Actions = CLI.actions
    for k in sorted(dir(conf_mod.Plugins.Actions)):
        if k == 'help' or k[0] == '_':
            continue
        h = True
        mod = getattr(plugins, k)
        doc = mod.__doc__ or ''
        if Actions and k == Actions[-1]:
            res.clear()
        run = getattr(mod, 'run', None)
        if not run:
            add('Not an action (no run method)', k)
        else:
            add('Action: %s' % k)
            add(doc)
            add(run.__doc__ or '')
            if Actions and k == Actions[-1]:
                hlp = getattr(mod, 'help', None)
                if hlp:
                    add(hlp())
                break
    print('\n'.join(res))
    if h:
        sys.exit(0)
    return
