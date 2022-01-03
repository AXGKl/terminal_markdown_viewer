from mdv import tools
from mdv.plugs import plugins


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


def run(dflt_out='-'):
    """
    Renders the source

    :param dflt_out [str]: API calls supply '' in order to supress printing.

    Returns the rendered html, as list of rows. 
    """

    p = plugins
    C = tools.C
    out = C['term_out']
    if not out:
        C['term_out'] = out = dflt_out
    src = C.get('src')
    if not src:
        tools.die('No md/html source given')
    parsed = p.mdparser.convert(src)
    fn = C.get('html_out')
    if fn:
        write_html(parsed, fn)
    # all the html tags have after this a .style property:
    dom = p.tree_analyzer.walk_tree(parsed)
    rows = p.render.visualize(dom)
    if C['ruler']:
        rows.insert(0, tools.ruler())
    if out:
        r = '\n'.join(rows)
        if out == '-':
            print(r)
        else:
            with open(out, 'w') as fd:
                fd.write(out)
    return rows
