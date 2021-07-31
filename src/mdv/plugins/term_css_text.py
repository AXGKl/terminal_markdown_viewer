"""
Lazy loaded module, only when content or counter css is present

There is a lot specified, but even browsers do not comply 100%.

For now we do whats needed to have numbered headers and lists with symbols.

- https://developer.mozilla.org/en-US/docs/Web/CSS/content
- https://developer.mozilla.org/en-US/docs/Web/CSS/counter-reset

"""
from functools import partial

from mdv import tools

# all css counters:
Counters = {}


def handle_counter(s, _cnt={'counter-increment': 1, 'counter-decrement': -1}):
    d = s._
    cr = d.get('counter-reset')
    if cr:
        cr = (cr + ' 0').split()[:2]
        Counters[cr[0]] = int(cr[1])
    offs = None
    for k in _cnt:
        if k in d:
            v = d[k]
            try:
                Counters[v] += _cnt[k]
            except:
                Counters[v] = 0
                Counters[v] += _cnt[k]


def content_with_counters(s, txt, T):
    # TODO: clear this quickhack
    for c in Counters:
        if c in T:
            T = T.replace('counter(%s)' % c, str(Counters[c]))
    T = T.replace('"', '')
    return T


def content(s, _n={'normal', 'none'}):
    d = s._
    T = d['content'] if 'content' in d else None
    if not T or not 'counter' in T:
        return T
    return partial(content_with_counters, T=T)


def post_import():
    S = tools.plugins.style.Style
    tools.make_cached_property(S, content, 'content')
    setattr(S, 'handle_counter', handle_counter)


hooks = {'post_import': post_import}
