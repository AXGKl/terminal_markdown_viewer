from mdv import tools


def show(c, r, p, n):
    r.append(p + ' ' + n)
    for k in sorted(dir(c)):
        if k[0] == '_':
            continue
        v = getattr(c, k)
        if isinstance(v, type):
            show(v, r, p + '#', k)
            continue
        r.append('- %s: %s' % (k, str(v)))


def run():
    f = tools.FileConfig[0]
    p = '#'
    r = []
    show(f, r, p, 'mdv2')
    print('\n'.join(r))
