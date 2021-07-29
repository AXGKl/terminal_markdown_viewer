"""
Produces color tables on stdout
"""

from mdv import tools
from mdv.plugins import color_table_256, color_table_256_true


def colors_4():
    return dict([(str(k - 10) + '   ', str(k)) for k in range(40, 48)])


def colors_8():
    return color_table_256.colors


def colors_8_true():
    return color_table_256_true.colors


def colors_24():
    return tools.plugins.colors_web.colors


W = [0]

tables = [
    [
        '24 Bit (Web) Colors',
        'CSS e.g. {color: rgb(255, 0, 0)} or #F00 or hsl() or name...',
        colors_24,
        '48;2;',
    ],
    [
        '8 Bit Colors Absolute',
        'Config: color_table_256_true, then CSS: e.g. {color: ansi(9)})',
        colors_8_true,
        '48;2;',
    ],
    ['8 Bit Colors, 0-15 Themable', 'CSS: {color: ansi(<0-255>)}', colors_8, '48;5;'],
    ['3/4 Bit Colors', 'CSS: {color: ansi("<30-37>")}', colors_4, ''],
]


def add_table(title, subt, table, r, prefix, max_, filt):
    title = title.ljust(W[0])
    r.extend(['\n\n\x1b[1;47;30m', title, '\x1b[0m\n'])
    r.extend([subt, '\n'])
    l = max([len(k) for k in table])
    cols = int(W[0] / l) - 1
    colors = []
    add = r.append

    def flush_colors():
        add('\n')
        r.extend(colors)
        colors.clear()
        add('\n')
        return 0

    i = -1
    j = 0
    msg = ''
    for k, v in table.items():
        if filt and not filt in k and not filt in str(v):
            continue
        i += 1
        j += 1
        if j > max_ and max_:
            msg = '(%s more colors)' % (len(table) - j)
            break
        if i > cols:
            i = flush_colors()

        add(('%s                        ' % k)[:l])
        colors.append('\x1b[%s%sm%s\x1b[0m ' % (prefix, v, ' ' * (l - 1)))
    flush_colors()
    if msg:
        r.append(msg)


def run(filter='', max=0):
    """
    Displays Various Colortables on stdout

    - filter: When supplied we skip non matching entries. If a title matches we don't
      display the others but all colors within the matching table.
    - max: Maximum entries displayed per table
    """
    r = []
    W[0] = tools.C['width']
    for title, subt, func, prefix in tables:
        table = func()
        if filter and filter in title:
            r.clear()
            filter == False
        add_table(title, subt, table, r, prefix, max, filter)
        if filter == False:
            break

    print(''.join(r))
