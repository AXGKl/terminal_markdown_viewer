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

hex_prefix = {
    'fg': '38;2;',
    'bg': '48;2;',
}

fmts = '%s%s'
fmtr = '%s;%s;%s'


def ansi(*a):
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


def set_col(css, k, v):
    if not v:
        return
        breakpoint()  # FIXME BREAKPOINT
    if v[0] == '#':
        pref = hex_prefix
        if len(v) == 4:
            v = v[1] + v[1] + v[2] + v[2] + v[3] + v[3]
        else:
            v = (v + '99999999')[1:7]
        code = (int(v[i : i + 2], 16) for i in (0, 2, 4))
        code = fmtr % tuple(code)
    else:
        code = None
        for set in color_code_sets:
            pref, codes = set.colors
            code = codes.get(v)
            if code:
                break
        if not code:
            if '(' in v:
                try:
                    f, args = v.strip()[:-1].split('(', 1)
                    args = args.replace('%', '').replace('deg', '')  # hsl = 100[deg], ..
                    if not ',' in args:
                        args += ','
                    rgb = col_funcs[f](*literal_eval(args))  # security. no eval.
                    if f == 'ansi':
                        css[k] = rgb
                        return
                    code = fmtr % rgb
                except:
                    pass
        if not code:
                tools.die('Not supported color', color=v)
    fgbg = 'bg' if k == 'background-color' else 'fg'
    css[k] = fmts % (pref[fgbg], code)


def load_color_codes():
    color_code_sets.append(tools.plugins.color_ansi_base16)
    color_code_sets.append(tools.plugins.color_ansi_true_css_names)


def set_color(css):
    if not color_code_sets:
        load_color_codes()

    print('css', css)
    bc = border_colors if css.get('_has_border') else []
    for L in colors, bc:
        for k in L:
            try:
                v = css[k]
                set_col(css, k, v)
            except:
                pass
