plugin = 'mdparser'

from markdown import Markdown
from markdown.extensions import fenced_code, tables

from mdv import tools

# from markdown.treeprocessors import Treeprocessor


def convert(md):
    MD = Markdown(
        tab_length=int(tools.C['tab_length']),
        extensions=[
            # this,
            tables.TableExtension(),
            #'pymdownx.betterem',
            fenced_code.FencedCodeExtension(),
        ],
    )
    html = MD.convert(md)
    # to allow global styles:
    html = '<body>%s</body>' % html

    return html
