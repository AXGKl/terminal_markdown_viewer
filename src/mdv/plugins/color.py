import colorsys
from ast import literal_eval

from mdv import tools

colors = [
    'color',
    'background-color',
]
border_colors = [
    'border-right-color',
    'border-left-color',
    'border-bottom-color',
    'border-top-color',
]

col_true_prefix = {
    'fg': '38;2;',
    'bg': '48;2;',
}

col_256_prefix = {
    'fg': '38;5;',
    'bg': '48;5;',
}
col_8_prefix = {
    'fg': '3',
    'bg': '4',
}

fmts = '%s%s'
fmtr = '%s;%s;%s'


def ansi(k, *a):
    if not a:
        return
    if len(a) == 1:
        # 32 -> '38;5;32'
        if type(a[0]) == int:
            # ansi(124):
            return col_256_prefix['bg' if k == 'background-color' else 'fg'] + str(a[0])
        # ansi('32') -> take a as is
        return a[0]
    return ';'.join([str(i) for i in a])


def hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360.0, l / 100.0, s / 100.0)
    return rgb(r, g, b,)


def hls(h, l, s):
    return hsl(h, s, l)


def yiq(*a):
    r, g, b = colorsys.yiq_to_rgb(*a)
    return rgb(r, g, b)


def hsv(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, s / 100.0, v / 100.0)
    return rgb(r, g, b,)


def rgb(r, g, b):
    r = r if type(r) == int else int(r * 255)
    g = g if type(g) == int else int(g * 255)
    b = b if type(b) == int else int(b * 255)
    return r, g, b


col_funcs = {'ansi': ansi, 'hsl': hsl, 'hls': hls, 'yiq': yiq, 'rgb': rgb}

color_code_sets = []


def get_col(css, k, v, cache={}):
    try:
        return cache[v]
    except:
        pass
    if not v:
        return
    if type(v) == int:
        pref = col_256_prefix
        code = v

    elif v[0] == '#':
        # hex, 3 or 6 digit
        pref = col_true_prefix
        if len(v) == 4:
            v = v[1] + v[1] + v[2] + v[2] + v[3] + v[3]
        else:
            v = (v + '99999999')[1:7]
        code = (int(v[i : i + 2], 16) for i in (0, 2, 4))
        code = fmtr % tuple(code)

    elif open_bracket in v:
        # color function
        f, args = v.split('(', 1)
        f = f.strip()
        args = args.replace(')', '').strip()
        args = args.replace('%', '').replace('deg', '')  # hsl = 100[deg], ..
        if not ',' in args:
            args += ','
        args = literal_eval(args)
        i = 9 / 0
        if f == 'ansi':
            args = (k,) + args
        rgb = col_funcs[f](*args)  # security: no eval.
        if f == 'ansi':
            # just ;-joined values
            # user gave already bg or fg, we get sth like '38;5;124'
            cache[k] = rgb
            return rgb
        code = fmtr % rgb

    else:
        # shortcut for non css colors
        if ';' in v:
            cache[k] = v
            return v
        names = tools.plugins.color_table
        code = names.colors[v]
        if type(code) == int:
            pref = col_256_prefix
        elif ';' in code:
            pref = col_true_prefix
        else:
            pref = col_8_prefix
    fgbg = 'bg' if k == 'background-color' else 'fg'
    r = cache[k] = fmts % (pref[fgbg], code)
    return r


def load_color_codes():
    color_code_sets.append(tools.plugins.color_ansi_base16)
    color_code_sets.append(tools.plugins.color_ansi_true_css_names)


def set_color(css):
    load_color_codes()

    print('css', css)
    bc = border_colors if css.get('_has_border') else []
    for L in colors, bc:
        for k in L:
            try:
                v = css[k]
            except:
                continue
            try:
                v = get_col(css, k, v)
                if v is not None:
                    css[k] = v
            except Exception as ex:
                tools.log.warning('Color conversion problem', value=v)


# some pluging disturbs the IDE with this in the code. grrr:
open_bracket = '('
