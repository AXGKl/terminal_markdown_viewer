from mdv import tools


def write_html(html, fn):
    C = tools.C
    css = C.get('css_file')
    if css:
        css = tools.read_file(css)
    with open(fn, 'w') as fd:
        s = '''<html>
            <head>
            _SCR_
            <style>
            _ST_
            </style>
            <style>
            body {font-size:1em; font-family: monospace;}
            </style>
            </head>'''
        s = s.replace(' ', '').replace('_ST_', css)
        s = s.replace('_SCR_', '<script src="https://livejs.com/live.js"></script>')
        s += str(html) + '</html>'
        fd.write(s)

        # xbody {padding: 0px; font-size:1em; font-family: monospace;width: 30.08em !important; color: red;}
        # xp {background-color: green;}


def run():
    p = tools.plugins
    C = tools.C
    md = C.get('md')
    if not md:
        tools.die('No markdown given')
    parsed = p.mdparser.convert(md)
    fn = C.get('html')
    if fn:
        write_html(parsed, fn)
    tree = p.tree_analyzer.set_initial_styles(parsed)
    ansi = p.render.format(tree)
    return ansi
