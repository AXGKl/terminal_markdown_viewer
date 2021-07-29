from mdv import tools


def run():
    W = tools.C['width']
    len = 17
    cols = int(W / len) - 1
    b16 = tools.plugins.color_ansi_base16
    true = tools.plugins.color_ansi_true_css_names

    r = []
    add = r.append

    def do(m, cols=cols, len=len):
        a256 = False
        p, c = m.prefix['bg'], m.codes
        i = 0
        colors = []

        def flush_colors():
            add('\n')
            r.extend(colors)
            colors.clear()
            add('\n')
            return 0

        for k, v in c.items():
            i += 1
            if i > cols:
                i = flush_colors()
            # we have also the 256 colors in that mapping, as integers:
            if isinstance(k, int) and not a256:
                i = flush_colors()
                add('\nAnsi 256 Colors (Absolute. Any Terminal):\n')
                cols = int(W / 4) - 1
                len = 4
                a256 = True
            add(('%s                        ' % k)[:len])
            colors.append('\x1b[%s%sm%s\x1b[0m ' % (p, v, ' ' * (len - 1)))
        flush_colors()

    add('CSS (True) Color Names (Absolute. Require True Color Capable Terminal):\n')
    do(true)
    add('\n\n')
    add('Terminal Base16 Colors (Subject to  Terminal theme):\n')
    do(b16)

    print(''.join(r))
