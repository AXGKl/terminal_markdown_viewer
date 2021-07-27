"""
BS CSS selectors: From VS version 4.7:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
https://developer.mozilla.org/en-US/docs/Web/CSS/calc()
"""

plugin = 'tree_analyzer'

from bs4 import BeautifulSoup as BS

from mdv import tools

s = [0]


class BSMDV(BS):
    def __init__(self, *a, **kw):
        s = self._super = super(BSMDV, self)
        s.__init__(*a, **kw)

    def handle_starttag(self, name, *a, **kw):
        tag = self._super.handle_starttag(name, *a, **kw)
        tag.style = s[0](tag, name)
        return tag

    def handle_data(self, data):
        r = self._super.handle_data(data)
        return r

    def handle_endtag(self, name, *a, **kw):
        r = self._super.handle_endtag(name, *a, **kw)
        return r


def assign_css_rules(soup, style):
    for r in style.rules:
        sel, rules = r
        tags = soup.select(sel)
        if not tags:
            continue
        style.prepare_rule(r)  # shorthands resolution
        style.rules_in_use.append(r)
        for t in tags:
            t.style._.update(rules)


def set_initial_styles(html):
    style = tools.plugins.style
    s[0] = style.Style
    soup = BSMDV(html, 'html.parser')
    assign_css_rules(soup, tools.plugins.style)
    st = soup.style = style.DocumentStyle(soup, soup.name)
    soup.body.style.parent = st
    st.content_width = tools.C['width']
    st.content_height = tools.C['height']
    return soup.body