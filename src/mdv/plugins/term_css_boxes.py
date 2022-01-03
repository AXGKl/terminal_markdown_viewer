# coding: utf-8
# https://jrgraphix.net/r/Unicode/2500-257F
from mdv import tools
from functools import partial
from mdv.plugs import plugins

style = plugins.style
dirs = style.dirs
em = style.em

_ = dict
css_styles = {'solid', 'dashed', 'dotted', 'double'}

hb = ' ─━█┄╌╴╸┈┉┅╍═'
vb = ' │┃█╎╎╵╹┊┆┋┇║'
# TODO: dashed, dotted width 1
styles = [
    'solid0',
    'solid1',
    'solid2',
    'solid3',
    'dashed1',
    'dashed2',
    'dashed3',
    'dashed4',
    'dotted1',
    'dotted2',
    'dotted3',
    'dotted4',
    'double',
]
styles_count = range(len(styles))

# margin pading:
mp_by_box_char = {
    ' ': (1.0, 0.0),
    '─': (0.4, 0.4),
    '━': (0.2, 0.2),
    '█': (0.0, 0.0),
    '┄': (0.4, 0.4),
    '╌': (0.4, 0.4),
    '╴': (0.4, 0.4),
    '╸': (0.2, 0.2),
    '┈': (0.4, 0.4),
    '┉': (0.2, 0.2),
    '┅': (0.2, 0.2),
    '╍': (0.2, 0.2),
    '═': (0.3, 0.3),
    '│': (0.4, 0.4),
    '┃': (0.2, 0.2),
    '╎': (0.4, 0.4),
    '╎': (0.4, 0.4),
    '╵': (0.4, 0.4),
    '╹': (0.2, 0.2),
    '┊': (0.4, 0.4),
    '┆': (0.4, 0.4),
    '┋': (0.2, 0.2),
    '┇': (0.2, 0.2),
    '║': (0.3, 0.3),
}
# each *must 0.4, 0.4,  * provide a match for w=1, comp is '<':
s_by_max_w = {
    'solid': {0.1: 0, 0.3: 1, 0.4: 2, 1.01: 3},
    'dashed': {0.1: 'solid0', 0.2: 1, 0.3: 2, 0.4: 3, 1.01: 4},
    'dotted': {0.1: 'solid0', 0.2: 1, 0.3: 2, 0.4: 3, 1.01: 4},
    'double': {1.01: 'double'},
}


topleft = '''
   ─━█┄╌╴╸┈┉┅╍═
                   
 │ ┌┍ ┌┌┌┍┌┍┍┍╒                   
 ┃ ┎┏ ┎┎┎┏┎┏┏┏╒                             
 █ ▄▄█▄▄▄▄▄▄▄▄▄
 ╎ ┌┍ ┌┌┌┍┌┍┍┍╒                   
 ╎ ┌┍ ┌┌┌┍┌┍┍┍╒                   
 ╵ ┌┍ ┌┌┌┍┌┍┍┍╒                   
 ╹ ┎┏ ┎┎┎┏┎┏┏┏╒                             
 ┊ ┌┍ ┌┌┌┍┌┍┍┍╒                   
 ┆ ┌┍ ┌┌┌┍┌┍┍┍╒                   
 ┋ ┎┏ ┎┎┎┏┎┏┏┏╒                             
 ┇ ┎┏ ┎┎┎┏┎┏┏┏╒                             
 ║ ╓╓║╓╓╓╓╓╓╓╓╔ 
'''

topright = '''
   ─━█┄╌╴╸┈┉┅╍═
                    
 │ ┐┑ ┐┐┑┑┐┑┑┑╕
 ┃ ┒┓ ┒┒┒┓┒┓┓┓╕
 █ ▄▄█▄▄▄▄▄▄▄▄▄
 ╎ ┐┑ ┐┐┑┑┐┑┑┑╕
 ╎ ┐┑ ┐┐┑┑┐┑┑┑╕ 
 ╵ ┐┑ ┐┐┑┑┐┑┑┑╕
 ╹ ┒┓ ┒┒┒┓┒┓┓┓╕
 ┊ ┐┑ ┐┐┑┑┐┑┑┑╕ 
 ┆ ┐┑ ┐┐┑┑┐┑┑┑╕ 
 ┋ ┒┓ ┒┒┒┓┒┓┓┓╕ 
 ┇ ┒┓ ┒┒┒┓┒┓┓┓╕ 
 ║ ╖╖║╖╖╖╖╗╗╗╗╗





╖╖╖╖╗
'''

bottomright = '''
   ─━█┄╌╴╸┈┉┅╍═
                    
 │ ┘┙┙┘┘┘┙┘┙┙┙╛
 ┃ ┚┛┛┚┚┚┛┚┛┛┛╛
 █ ▀▀█▀▀▀▀▀▀▀▀▀
 ╎ ┘┙┙┘┘┘┙┘┙┙┙╛
 ╎ ┘┙┙┘┘┘┙┘┙┙┙╛
 ╵ ┘┙┙┘┘┘┙┘┙┙┙╛
 ╹ ┚┛┛┚┚┚┛┚┛┛┛╛
 ┊ ┘┙┙┘┘┘┙┘┙┙┙╛
 ┆ ┘┙┙┘┘┘┙┘┙┙┙╛
 ┋ ┚┛┛┚┚┚┛┚┛┛┛╛
 ┇ ┚┛┛┚┚┚┛┚┛┛┛╛
 ║ ╜╜║╜╜╜╜╜╜╜╜╝
'''

bottomleft = '''
   ─━█┄╌╴╸┈┉┅╍═
                    
 │ └┕┕└└└┕└┕┕┕╘
 ┃ ┖┗┗┖┖┖┗┖┗┗┗╘
 █ ▀▀█▀▀▀▀▀▀▀▀▀
 ╎ └┕┕└└└┕└┕┕┕╘
 ╎ └┕┕└└└┕└┕┕┕╘
 ╵ └┕┕└└└┕└┕┕┕╘
 ╹ ┖┗┗┖┖┖┗┖┗┗┗╘
 ┊ └┕┕└└└┕└┕┕┕╘
 ┆ └┕┕└└└┕└┕┕┕╘
 ┋ ┖┗┗┖┖┖┗┖┗┗┗╘
 ┇ ┖┗┗┖┖┖┗┖┗┗┗╘
 ║ ╙╙║╙╙╙╙╙╙╙╙╚
'''


def idx(spec):
    lines = spec.splitlines()
    m = {}
    for r in styles_count:
        R = styles[r]
        m[R] = n = {}
        for c in styles_count:
            n[styles[c]] = lines[r + 2][c + 2]
    return m


vstyles = dict(zip(styles, vb))
hstyles = dict(zip(styles, hb))
tl_styles = idx(topleft)
tr_styles = idx(topright)
br_styles = idx(bottomright)
bl_styles = idx(bottomleft)
d = 'solid0'


def box_char_1_cell(w, s):
    """
    E.g.: w = 0.9, s='dashed' => returns: 'dashed3'
    """
    while 1:
        ws = s_by_max_w.get(s)
        if ws:
            break
        s = 'solid'
    for mw in ws:
        if w < mw:
            v = ws[mw]
            return v if isinstance(v, str) else ('%s%s' % (s, ws[mw]))


def box_char(style, dir):
    s = getattr(style, 'border_%s_style' % dir, None)
    w = getattr(style, 'border_%s_width' % dir, None)
    if None in (s, w):
        return

    r = []
    while 1:
        w1 = min(1, w)
        r.append(box_char_1_cell(w1, s))
        if w <= 1:
            return list(reversed(r))
        w = w - 1


empty = ' '


def box_chars(t=d, r=d, b=d, l=d):
    tl = tl_styles[l][t]
    th = hstyles[t]
    tr = tr_styles[r][t]
    rv = vstyles[r]
    br = br_styles[r][b]
    bh = hstyles[b]
    bl = bl_styles[l][b]
    lv = vstyles[l]

    return (tl, th, tr, lv, rv, bl, bh, br)


# 0:top 1:right bottom left:
box_side_char_by_pos = {
    0: 1,
    1: 4,
    2: 6,
    3: 3,
}  # positions of the non corner chars in box_chars

char_by_name = {'top': 1, 'left': 3, 'right': 4, 'bottom': 6}


def box_by_style(style, _dirs=['top', 'right', 'bottom', 'left']):
    """
    Normal: all widths <=1 -> we return the set of characters for the box:
    <topleft, top, topright, left, right, bottomleft, bottom, bottomright>

    Feature: We support also widths > 1:
    When one width > 1, say 3.3, then we return 4 nestable box character sets

    style like:
        ... 
          border_left_width   : 1.3
          border_left_style   : solid
          # all others 0.2 dashed e.g.:
          border_right_width  : 0.2
          border_right_style  : dashed
    """
    # B: [['dashed2'], ['dashed2'], ['dashed2'], ['solid3', 'solid2']]
    B = [box_char(style, d) for d in _dirs]
    ml = max([len(i) for i in B])  # 2 in the example (1.3 -> requires 2 cells)
    R = []
    a = R.append
    s0 = 'solid0'
    for i in range(ml):
        t = B[0][i] if len(B[0]) > i else s0
        r = B[1][i] if len(B[1]) > i else s0
        b = B[2][i] if len(B[2]) > i else s0
        l = B[3][i] if len(B[3]) > i else s0
        a(box_chars(t=t, r=r, b=b, l=l))
    return R


dir_by_nr = {1: 'top', 3: 'left', 4: 'right', 6: 'bottom'}


def get_mp_adds(bcs, e=empty):
    m = {}
    for pos in 1, 3, 4, 6:
        L = []
        # itr = range(len(bcs) - 1, -1, -1) if outin else range(len(bcs))
        p = [0] if len(bcs) == 1 else [0, len(bcs) - 1]
        for l in p:
            k = bcs[l]
            c = k[pos]
            if c != e:
                L.append(mp_by_box_char[c])
            else:
                L.append((0, 0))
        m[dir_by_nr[pos]] = L[0][0], L[-1][-1]
    return m


def make_border(tag):
    """returns tuple (
        border_left_width, border_right_width
        function which renders top by padding box width
        left, right rendered border
        function which renders bottom by padding box width
        )
    """
    s = tag.style
    if not s._.get('_has_border'):
        return 0, 0, None, '', '', None

    bc = s.border_chars
    top, bottom, left, right = [], [], '', ''
    c = s.color
    btc = s.border_top_color
    bbc = s.border_bottom_color
    blc = s.border_left_color
    brc = s.border_right_color
    c = toansi
    # sides: easy, constant independent of width:
    for l in bc:
        # one rectangle
        if l[3] != empty:
            left += l[3]
        if l[4] != empty:
            right = l[4] + right
    ll, lr = len(left), len(right)
    lbl, lbr = '', ''  # for width > 1 borders these are the left right parts
    lbi, lbj = 0, lr
    i = -1

    # this is hard, due to side border fragments we need at the corners
    # We can have >1em wide borders on any side. border chars e.g:
    # [('╔', '═', '╗', '║', '║', '╚', '═', '╝'), # outest border
    #  (' ', ' ', ' ', '║', '║', ' ', ' ', ' '), # inside first

    for l in bc:
        i += 1
        # print(i, '-', lbl, '-', lbr, '-', left, '-', right)
        t = l[1]
        if t != empty:
            # 0, 2: the corners
            l0 = l[0] if l[0] != empty else ''
            l2 = l[2] if l[2] != empty else ''
            v = (lbl, l0 + (ll - 1) * t, t, t * (lr - 1) + l2, lbr)
            top.append(v)
        t = l[6]
        if t != empty:
            l5 = l[5] if l[5] != empty else ''
            l7 = l[7] if l[7] != empty else ''
            v = (lbl, l5 + (ll - 1) * t, t, t * (lr - 1) + l7, lbr)
            bottom.insert(0, v)
        ll = max(0, ll - 1)
        lr = max(0, lr - 1)
        lbi += 1
        lbj = max(0, lbj - 1)
        lbl = c(left[:lbi], blc)
        lbr = c(right[lbj:], brc)

    def top_(w, top=top, c=c, col=btc):
        return [l[0] + c(l[1] + w * l[2] + l[3], col) + l[4] for l in top]

    def bottom_(w, bottom=bottom, c=c, col=bbc):
        return [l[0] + c(l[1] + w * l[2] + l[3], col) + l[4] for l in bottom]

    return len(left), len(right), top_, c(left, blc), c(right, brc), bottom_


toansi = lambda s, col: '\x1b[%sm%s\x1b[0m' % (col, s)


# ------------------------------------------------------------------------- Style Props


def border_dir_width(s, dir):
    try:
        w = em(s._['border-%s-width' % dir], outer=s._parent_content_width)
        if w < 0.1:
            return 0
        return w
    except:
        return 0


def border_style(s, dir):
    try:
        w = s._['border-%s-style' % dir]
        return w
    except:
        return None


def border_color(s, dir):
    try:
        w = s._['border-%s-color' % dir]
    except:
        w = s.color
    # when we are > 1 em we take the outside background, else the inner (if set)
    if getattr(s, 'border_%s_width' % dir) > 0:
        bg = s.parent.background_color
    else:
        bg = s.background_color  # when not set its outside
    # when w is an ansi() incl. bg it will be overrulling the bg:
    return (bg + ';' + w) if bg else w


def rendered_border(s):
    return make_border(s.tag)


def border_width(s):
    if not s._.get('_has_border'):
        return 0
    R = box_by_style(s)
    s._mp_add_from_border = get_mp_adds(R)
    s.border_chars = R
    return int(s.border_left_width + 0.99) + int(s.border_right_width + 0.99)


def post_import():
    mcp = tools.make_cached_property
    cp = tools.cached_property
    Style = style.Style
    mcp(Style, border_width, 'border_width')
    mcp(Style, rendered_border, 'rendered_border')
    for d in dirs:
        b = f'border_{d}_'
        mcp(Style, border_dir_width, b + 'width', d)
        mcp(Style, border_style, b + 'style', d)
        mcp(Style, border_color, b + 'color', d)


hooks = {'post_import': post_import}


# begin_archive
# e.g. "|" already provides some margin and padding left and right:
# cs._box_char_mp_adds = d['_margin_adds'], d['_padding_adds']


#     # R:   tl    t    tr   l    r    bl   b    br
#     #    [('▄', '╌', '┐', '█', '╎', '▀', '╌', '┘'),  outest
#     #     (' ', ' ', ' ', '┃', ' ', ' ', ' ', ' ')]  innerst
#     # -> margin left addition is now 0 for left, 0.4 for all other dirs
#     # -> padding left addition is  0.4 for left (second row),
#     # 0.4 for all other dirs (first row, second is empty for those)
#     ma = [(), (), (), ()]
#     mp = [(), (), (), ()]
#     for d in range(4):
#         p = box_side_char_by_pos[d]
#         for l in R:
#             c = l[p]
#             if c == empty:
#                 continue
#             ma[d] += (l[p],)
#             mp[d] += (l[p],)
#     # ma e.g.: [('╌',), ('╎',), ('╌',), ('█', '┃')]

#     ma = [mp_by_box_char[t[0]] for t in ma]
#     mp = [mp_by_box_char[t[-1]] for t in mp]
#     MA, MP = [0, 0, 0, 0], [0, 0, 0, 0]
#     for d in range(4):
#         c = ma[d][0]
#         if c:
#             MA[d] = c
#         c = mp[d][-1]
#         if c:
#             MP[d] = c

#     # (Pdb) pp MA, MP
#     # [0.4, 0.4, 0.4, 0], [0.4, 0.4, 0.4, 0.2] (left 0 and 0.2 because outest box has '█' on the left and innerst box has '┃' on the left)
#     return {'_box_chars': R, '_margin_adds': MA, '_padding_adds': MP}


# reset = '\x1b[0m'


# def combine_ansi(l):
#     r = []
#     for k in l:
#         a = k.get('ansi')
#         if a and a not in r:
#             r.append(a)
#     return ';'.join(r)


# debug = False
# default_min_width = 10
# SPCPH = '\u00A0'


# is_side = lambda d, lr={'left', 'right'}: d in lr


# class Box:
#     mbp_width = None
#     width = None

#     def __init__(self, style):
#         """
#         style like: [
#             {'ansi': '38;5;124',
#              'border': '2 solid H1',
#              'border-bottom-ansi': '1;33',
#              'border-chars': ('┏', '━', '┓', '┃', '┃', '┗', '━', '┛'),
#              'border-left-ansi': '1;33',
#              'border-right-ansi': '1;33',
#              'border-top-ansi': '1;33',
#              'esc': functools.partial(<function AEsc at 0x7f5c7db19280>, ansi_='38;5;124'),
#              'has_box': True}
#         ]

#         """
#         self.fmt = style[-1]
#         self.min_width = self.fmt.get('min-width', default_min_width)
#         self.style = style
#         self.setup()
#         self.inner_width = lambda w: w - self.mbp_widths()

#     def mbp_widths(self):
#         return sum(self.mbp_width.values())

#     def reset(self):
#         """
#         self.frame = {'left': [margl, borderl, paddl], 'right': [paddr, borderr, margr], ...}
#         i.e. reversed mbp for right and bottom
#         """
#         self.frame = {'left': [], 'right': [], 'top': [], 'bottom': []}
#         self.mbp_width = {'margin': 0, 'border': 0, 'padding': 0}

#     def setup(self, narrow=False):
#         self.reset()
#         # calc sides first, to be able to calc top and bottom:
#         for d in 'left', 'right', 'top', 'bottom':
#             # narrow is set at set_width, when inner_width < min-width.
#             # Then we completely drop sides TODO: make that 3 step, dropping margin and padding only first
#             if narrow and is_side(d):
#                 self.frame[d] = ['', '', '']
#                 if d == 'left':
#                     bc = self.fmt['border-chars']
#                     l = '', bc[1], '', bc[3], bc[4], '', bc[6], ''
#                     self.fmt['border-chars'] = l
#                 continue

#             for f in self.setup_margin, self.setup_border, self.setup_padding:
#                 s = f(d)
#                 if d in {'left', 'top'}:
#                     self.frame[d].append(s)
#                 else:
#                     # padding border margin
#                     self.frame[d].insert(0, s)

#     def setup_border(self, d):
#         bc = self.fmt.get('border-chars')
#         if not bc:
#             return ''
#         ansi = self.fmt.get('border-%s-ansi' % d, '')
#         if is_side(d):
#             c = bc[3] if d == 'left' else bc[4]
#             if not c or c == ' ':
#                 return ''
#             # border is max 1 cell
#             self.mbp_width['border'] += 1
#             return '\x1b[%sm%s%s' % (ansi, c, reset)

#         # 'border-chars': ('┌', '─', '┐', '█', '╎', '└', '─', '┘'),
#         mr = ml = cl = cr = ''
#         j = 0 if d == 'top' else 5  # pick the characters from border-chars
#         cs = bc[j : j + 3]
#         if not cs[1] or cs[1] == ' ':
#             return ''
#         # build top / bottom border with corner chars:
#         ml = self.frame['left'][0] or ''  # margin left
#         cl = cs[0].strip()
#         # w = what we subtract from total width later once known:
#         w = self.mbp_widths() - self.mbp_width['padding']
#         txt = '_W_:%s:%s_W_' % (w, cs[1])
#         mr = self.frame['right'][2] or ''  # margin right
#         cr = cs[2].strip()
#         s = ''.join([cl, txt, cr])
#         return '%s\x1b[%sm%s%s%s' % (ml, ansi, s, reset, mr)

#     def setup_margin_or_padding(self, d, is_margin=True):
#         n = 'margin' if is_margin else 'padding'
#         if not is_margin and 0:
#             breakpoint()  # FIXME BREAKPOINT
#         N = n + '-' + d
#         L = R = ''
#         v = self.fmt.get(N)  # for padding and margin just a number
#         if not v:
#             return ''
#         ansi = combine_ansi(self.style[: -1 if is_margin else 0])
#         c = n[0] if debug else SPCPH  # in debug mode we print m or p instead spaces
#         if is_side(d):
#             self.mbp_width[n] += v
#             txt = c * v
#         else:
#             w = 0 if n == 'margin' else self.mbp_widths()
#             txt = '_W_:%s:%s_W_' % (w, c.upper())
#             if not is_margin:
#                 L = ''.join(self.frame['left'])
#                 R = ''.join(self.frame['right'])
#         return L + '\x1b[%sm%s%s' % (ansi, txt, reset) + R

#     def setup_margin(self, d):
#         return self.setup_margin_or_padding(d)

#     def setup_padding(self, d):
#         return self.setup_margin_or_padding(d, is_margin=False)

#     def set_width(self, width):
#         """
#         min inner: We drop left / right framing if too narrow for text
#         """
#         ret = {'left': '', 'right': '', 'top': [], 'bottom': []}
#         for d in 'left', 'right', 'top', 'bottom':
#             # top:
#             frame = self.frame[d]
#             for t in frame:
#                 if not t:
#                     continue
#                 if d in ('top', 'bottom'):
#                     try:
#                         pre, m, post = t.split('_W_')
#                     except Exception as ex:
#                         print('breakpoint set')
#                         breakpoint()
#                         keep_ctx = True
#                     m = m.split(':')
#                     ret[d].append(pre + (width - int(m[1])) * m[2] + post)
#                 else:
#                     ret[d] += t if t else ''
#         self.tmpl = ret
#         self.width = width
#         self._inner_width = iw = self.inner_width(width)
#         mw = min(self.min_width, width)
#         if iw < mw:
#             self.setup(narrow=True)
#             self.set_width(width)

#     def draw(self, txt=None, width=None, printout=False, txt_is_ansi=True, ls=''):
#         out = []
#         if width and width != self.width:
#             self.set_width(width)
#         width = self.width
#         iw = self.inner_width(width)
#         if txt == None:
#             txt = iw * SPCPH
#         if isinstance(txt, str):
#             txt = txt.split('\n')
#         for l in self.tmpl['top']:
#             out.append(l + ls)
#         L, R = self.tmpl['left'], self.tmpl['right']
#         for line in txt:
#             # cut off if too long and text not already ansi:
#             l = line if txt_is_ansi else line.ljust(iw)[:iw]
#             out.append(L + l + R + ls)
#         for l in self.tmpl['bottom']:
#             out.append(l + ls)
#         if printout:
#             [print(i, end='') for i in out]
#         return out

#     def print(self, txt, width=None):
#         self.draw(txt, width=width, printout=True, txt_is_ansi=False, ls='\n')


# def insert(l, s):
#     l.insert(0, s)


# def append(l, s):
#     l.append(s)


# def box_maker(style):

#     """returns a function, which makes a box by width"""
#     # fast path:
#     try:
#         fmt = style[-1]
#     except Exception as ex:
#         print('breakpoint set')
#         breakpoint()
#         return
#         keep_ctx = True
#     if not fmt.get('has_box'):
#         return
#     return Box(style)  # .draw(100, 100)


# class boxpos:
#     top_left, top, top_right, left, right, bottom_left, bottom, bottom_right = range(8)


if __name__ == '__main__':
    pass
