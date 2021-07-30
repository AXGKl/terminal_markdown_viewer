"""
Lazy loaded module, only when content or counter css is present
"""
from mdv import tools

# all css counters:
Counters = {}

def content(s, _cnt={'counter-increment', 'counter-decrement'}, _n={'normal', 'none'}):
    d = s._
    T = d['content'] if 'content' in d else None
    if 'counter-reset' in d:
        Counters[d['counter-reset']] = 0
    cid = {}
    for k in _cnt:
        if k in d:
            cid[k] = d[k]
    if not T and not cid:
        return None

    def f(s, txt, T=T, cid=cid):
        for k, v in cid.items():
            if not v in Counters:
                continue
            Counters[v] += 1 if k == 'counter-increment' else -1
        if not T:
            return txt
        if T in _n:
            return ''
        # content: counter(h2counter) ".\0000a0\0000a0";
        # TODO: clear this quickhack
        for c in Counters:
            if c in T:
                T = T.replace('counter(%s)' % c, str(Counters[c]))
        T = T.replace('"', '')
        return T

    return f


def post_import():
    tools.make_cached_property(tools.plugins.style.Style, content, 'content')


hooks = {'post_import': post_import}
