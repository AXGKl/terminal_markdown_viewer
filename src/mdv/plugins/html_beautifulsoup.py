"""
BS CSS selectors: From VS version 4.7:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
https://developer.mozilla.org/en-US/docs/Web/CSS/calc()
"""

plugin = 'tree_analyzer'

from bs4 import BeautifulSoup as BS
from soupsieve import css_parser

from mdv import tools
from mdv.plugs import plugins

css_parser.PSEUDO_SUPPORTED.add(':before')


s = [0]


class BSMDV(BS):
    def __init__(self, *a):
        self.style = plugins.style
        s = self._super = super(BSMDV, self)
        self.log = tools.log.debug
        s.__init__(*a)

    def handle_starttag(self, name, *a, **kw):
        self.log('handle_starttag <%s>' % name)

        tag = self._super.handle_starttag(name, *a, **kw)
        # maybe useful someday (editor link, whatever) but md pos missing
        tag.html_pos = kw
        d = None
        if tag.has_attr('style'):
            d = tag.get_attribute_list('style')
            if d:
                d = self.style.get_elmt_style(d[0])

        # TODO perf: reuse built style objects (!!!!) (when width equal)
        tag.style = self.style.Style(tag, name, elmt_style=d)
        return tag

    # def handle_data(self, data):
    #     r = self._super.handle_data(data)
    #     return r

    def handle_endtag(self, name):
        self.log('handle_endtag </%s>' % name)
        if name == 'style':
            # inline style:
            self.style.add_inline_style_tag(self.current_data)
        r = self._super.handle_endtag(name)
        return r


def assign_css_rules(soup, style):
    for r in style.rules:
        pseudo = None
        sel, settings = r

        if ':' in sel and not sel[0] == ':':
            # pseudo
            sel, pseudo = sel.split(':', 1)
        tags = soup.select(sel)
        if not tags:
            continue
        style.prepare_css(r[1])  # shorthands resolution
        style.rules_in_use.append(r)
        for t in tags:
            if pseudo:
                t.style._.setdefault(pseudo, {}).update(settings)
            else:
                # element style rules over css files and theme:
                k = dict(t.style._)
                t.style._.update(settings)
                t.style._.update(k)


def walk_tree(html):
    # this has the default style rules (from theme and css file)
    style = plugins.style
    # same selectors are unified, containing all style infos:
    style.merge_same_selector()
    # this walks the html tree and builds a DOM
    # inline styles are already detected and parsed:
    soup = BSMDV(html, 'html.parser')
    # go through all style rules, select all tags and apply the style:
    assign_css_rules(soup, plugins.style)
    # We need a root parent style:
    st = soup.style = style.DocumentStyle(soup, soup.name)
    soup.body.style.parent = st
    st.content_width = tools.C['width']
    st.content_height = tools.C['height']
    return soup.body
