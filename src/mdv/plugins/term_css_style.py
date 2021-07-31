"""
CSS for the Terminal

This takes care for all the computed styles, from the initial CSS.
"""

from functools import partial

# ----------------------------------------------------- Time 3: OUTER BLOCK WIDTH KNOWN
from mdv import tools

cached_property = tools.cached_property

# Percent = tools.Percent
px_per_em = 16.0

rules = []
rules_in_use = []
render_mode = {'per_cell': False}  # only when we have overlays

C = tools.C

font_weights = {'bold': 1, 'bolder': 1, 'lighter': 2, 'normal': 0}
dirs = {'top', 'right', 'bottom', 'left'}
mbp = {'margin', 'border', 'padding'}

g = lambda o, k, d=None: getattr(o, k, d)

calced_style_by_pth = {}

type_none = type(None)
type_int = type(int)


def em(v, outer=None):
    if type(v) == str:
        if v[-2:] == 'em':
            return float(v.replace('em', ''))
        if v[-1:] == '%':
            return outer / 100 * float(v[:-1])
        if v[-1:] == 'px':
            return float(v[:-2] / px_per_em)
        return float(v)
    if type(v) == float:
        return v
    if type(v) == int:
        return v
    tools.die('Width not understood', width=v)


class Style:
    _mp_add_from_border = None

    def __init__(self, tag, name, elmt_style=None):
        self.tag = tag
        if tag.parent:
            self.parent = tag.parent.style
            self._ = {'display': 'block' if not name in inline_tags else 'inline'}
        self._.update(elmt_style) if elmt_style else None

    def __repr__(self):
        n = self.tag.name
        return '{style of %s}' % n

    @cached_property
    def box_sizing(self):
        return self._.get('box-sizing', 'content-box')

    @cached_property
    def content_width(s):
        W = s._parent_content_width = s.parent.content_width
        # first since the border character might influence margin
        bw = 0
        bw = s.border_width
        ow = s.outer_width
        return ow - s.margin_left - s.margin_right - s.padding_left - s.padding_right - bw

    @cached_property
    def outer_width(s):
        """with margin"""
        # often needed, we store:
        w = s._.get('width')
        W = s._parent_content_width
        if not w:
            return W
        # width was given:
        w = int(em(w, outer=W) + 0.99)
        if s.box_sizing == 'content-box':
            w += s.padding_left + s.padding_right + s.border_width
        if not W - w:
            ml, mr = 0, 0
        else:
            # overdetermined? adjust margins, given width rules:
            ml, mr = s.margin_left, s.margin_right
            D = W - w - ml - mr
            ml += max(0, int(D / 2))
            mr = W - w - ml
        s.margin_left = ml
        s.margin_right = mr
        return W

    @cached_property
    def display(self):
        return self._['display']

    @cached_property
    def font_weight(s, _fwa={None, '', 1, 2}, _fwn=font_weights):
        v = s._.get('font-weight', s.parent.font_weight)
        if v in _fwa:
            return v
        k = _fwn.get(v)
        if k is not None:
            return k
        v = int(v)
        if v < 350:
            return 2
        if v > 600:
            return 1
        return 0

    @cached_property
    def font_style(s, _st={'italic', 'oblique', 3}):
        v = s._.get('font-style', s.parent.font_style)
        if v in _st:
            return 3

    @cached_property
    def text_decoration(s, _st={'line-through': 9, 'underline': 4, 'blink': 5}):
        # browser adds them up:
        v, p = s._.get('text-decoration'), s.parent.text_decoration
        if not v:
            return p
        r = ''
        for k in v.split():
            try:
                r += ';%s' % _st[k]
            except:
                pass
        if r:
            r = r[1:]
        if p:
            r = p + ';' + r
        return r

    @cached_property
    def color(s):
        v = s._.get('color', s.parent.color)
        return v

    @cached_property
    def background_color(s):
        v = s._.get('background-color', s.parent.background_color)
        return v

    @cached_property
    def vertical_align(s):
        return s._.get('vertical-align', s.parent.vertical_align)

    def text_pre_wrap(s, txt, _sub={'sub', 'super'}):
        """Before we wrap we call this -> may modify text len"""

        if '_has_counter' in s._:
            s.handle_counter()

        if 'content' in s._:
            cf = s.content
            if isinstance(cf, str):
                txt = cf
            elif callable(cf):
                txt = cf(s, txt)

        # cf = s.content
        # if cf:
        #     txt = cf(s, txt)
        txt = rm_white_space(txt)
        va = s.vertical_align
        if va in _sub:
            txt = textmap(txt, mode=va)
        return txt

    @cached_property
    def cell_formatting_codes(s):
        """after we wrapped we call this - can't modify length
        -> independent of txt itself -> no func return"""
        a = ''
        v = s.font_weight
        if v:
            a += f'{v};'
        v = s.font_style
        if v:
            a += f'{v};'
        v = s.text_decoration
        if v:
            a += f'{v};'
        v = s.color
        if v:
            a += f'{v};'
        v = s.background_color
        if v:
            a += f'{v};'
        if a:
            a = a[:-1]
        return a or None

    def format_txt(s, txt):
        a = s.cell_formatting_codes  # cached
        if not a:
            return txt
        return f'\x1b[{a}m{txt}\x1b[0m'


class DocumentStyle(Style):
    font_weight = None
    color = None
    background_color = None
    font_style = None  # italic or oblique (also italic)
    text_decoration = None  # line-through blink underline
    vertical_align = None  # sub super


def textmap(txt, mode):
    t = tools.plugins.textmaps.transl.get(mode)
    if not t:
        return txt
    r = ''.join([t.get(k) or t.get(k.upper()) or t.get(k.lower(), k) for k in txt])
    return r


def rm_white_space(txt):
    return txt.replace('\n', ' ').replace('  ', ' ')


# props for all 4 directions:


def marg_padd(s, typ, d, pos_={'margin': 0, 'padding': 1}):
    a = s._mp_add_from_border
    a = a[d][pos_[typ]] if a else 0
    W = s._parent_content_width
    try:
        v = em(s._[typ + '-' + d], outer=W)
        v = int(v - a + 0.99)
        return v
    except:
        return 0


mcp = tools.make_cached_property
for d in dirs:
    mcp(Style, marg_padd, 'margin_' + d, 'margin', d)  # top, left, ...
    mcp(Style, marg_padd, 'padding_' + d, 'padding', d)


# --------------------------------------------------------------------------- Shorthands


def resolve_shorthands(css):
    w, s, c = set_border_shorthand(css, 'border', 0, '', '')
    for d in dirs:
        set_border_shorthand(css, 'border-' + d, w, s, c)
    set_marg_padd_shorthands(css)


def set_marg_padd_shorthands(css):
    for k in 'margin', 'padding':
        V = css.get(k)
        for d in dirs:
            n = k + '-' + d
            v = css.get(n, V)
            if v:
                css[n] = v


def set_border_shorthand(css, pref, w, s, c):
    g = css.get
    W = g(pref + '-width', w)
    S = g(pref + '-style', s)
    C = g(pref + '-color', c)
    v = g(pref)  # shorthand?
    if v:
        l = v.split(' ', 2)
        if len(l) == 3:
            W, S, C = l
        elif len(l) == 2:
            W, S = l
        else:
            S = l
    if W:
        # if pref != 'border':
        #     if 'right' in pref or 'left' in pref:
        #         a = css._max_mbp['width'][1]
        #     else:
        #         a = css._max_mbp['height'][1]
        css[pref + '-width'] = W
    if S:
        css[pref + '-style'] = S
    if C:
        css[pref + '-color'] = C
    if W or S or C:
        css['_has_border'] = True
    return W, S, C


# def inner_width(tag):
#     breakpoint() # FIXME BREAKPOINT
#     s = tag.style
#     d = boxes.box_by_css(s)


# ------------------------------------------------------------------------------: Import
cssutils_ = [0]

inline_tags = set()


def cheap_media_query_match(r):
    # cssutils does not give us any parsing(?), so...:
    # TODO: understand OR max-width
    t = str(r).split('mediaText=', 1)
    if len(t) < 2:
        return
    t = t[1].lower()
    if 'not tty' in t:
        return
    if 'only' in t and not 'only tty' in t:
        return
    for h in 'width', 'height':
        n = 'max-' + h + ':'
        if n in t:
            try:
                w = em(t.split(n, 1)[1].split(')', 1)[0].strip())
                if w < tools.C[h]:
                    return
            except:
                pass
    return True


def import_css_utils():
    import cssutils  # not always needed

    cssutils_[0] = cssutils
    return cssutils


def parse_css_string(s):
    cu = cssutils_[0] or import_css_utils()
    css = cu.parseString(s)
    register_css_rules(css)


def parse_css_file(fn):
    cu = cssutils_[0] or import_css_utils()

    # a few additional properties:
    mdv_profile = {'_have_mbp': '{ident}'}

    cu.profile.addProfile('mdv', mdv_profile)
    try:
        css = cu.parseFile(fn)
    except Exception as ex:
        tools.die('Cannot parse css file', exc=ex)
    register_css_rules(css)


def add_rule(r, parent=None):
    d = dict(r.style)
    if parent:
        d['_parent_rule'] = parent
    rules.append((r.selectorText, d))
    # no need to query for all kinds of props when none is there, for:
    # set _has_border _has_counter:
    for k in 'counter', 'border':
        if k in r.style.cssText:
            d['_has_%s' % k] = True


def register_css_rules(css):
    # TODO: lazy load these only when actual props are active!
    tools.plugins.boxes
    tools.plugins.term_css_text

    for r in css:
        if r.type == 1:
            # we work with dicts not attrs (['font-size'] instead .fontSize:
            add_rule(r)
        elif r.type == 4:
            # this is a media query css rule - does our current media match?
            if not cheap_media_query_match(r):
                continue
            # these are the rules within the media query, we append them:
            for k in r.cssRules:
                if k.type == 1:
                    add_rule(k, r)


# --------------------------------------------------------------------------- Rules
def prepare_css(css):
    # sel, css = rule
    resolve_shorthands(css)
    tools.plugins.color.set_color(css)
    return css
    # can't do more here - widths might be % based, so can't be calced w/o knowing outer
    # width.


sources = []


def get_elmt_style(content):
    css = dict(cssutils_[0].parseStyle(content))
    return prepare_css(css)


def add_inline_style_tag(content):
    """<style> within markdown or html"""
    sources.append('inline')
    parse_css_string(content[0])


def merge_same_selector():
    """we normally will have a theme and we possibly have inline styles
    Lets consolidate equal selector rules to one - saving soupsieve some selection
    effort on the same selectors later:
    """
    # sources like ['theme', 'inline']
    if len(sources) < 2:
        return
    have = {}
    r = []
    for k in rules:
        d = have.get(k[0])
        if d is not None:
            d.update(k[1])
        else:
            have[k[0]] = k[1]
            r.append(k)
    rules.clear()
    rules.extend(r)


def post_import():
    C = tools.C
    [inline_tags.add(k) for k in C['inline_tags']]
    fn_css = C['css_file']
    theme = C['theme']
    b = tools.plugins.boxes
    if theme:
        sources.append('theme')
        rules.extend(tools.plugins.theme.rules)
    # TODO load base vars
    # Tags[0] = tags(C=tools.C, Tag=Tag)

    if fn_css:
        sources.append('file')
        parse_css_file(fn_css)


hooks = {'post_import': post_import}
