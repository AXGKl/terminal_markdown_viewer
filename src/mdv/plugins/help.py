from mdv import tools

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
    f = tools.FileConfig[0]
    p = '#'
    r = []
    show(f, r, p, 'mdv2')
    print('\n'.join(r))
