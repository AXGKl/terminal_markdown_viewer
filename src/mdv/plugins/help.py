import sys

from mdv import tools
from mdv.plugs import plugins

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
    print('\nParameters:\n')
    conf_mod = plugins.config
    p = '#'
    r = []
    show(conf_mod, r, p, 'mdv2')
    print('\n'.join(r))
    print('\nActions:\n')
    for k in sorted(dir(conf_mod.Plugins.Actions)):
        if k == 'help' or k[0] == '_':
            continue
        h = True
        mod = getattr(plugins, k)
        doc = mod.__doc__ or ''
        run = getattr(mod, 'run', None)
        if not run:
            print('Not an action (no run method)', k)
        print('Action: ', k)
        print(doc)
        print(run.__doc__ or '')
    if h:
        sys.exit(0)
    return
