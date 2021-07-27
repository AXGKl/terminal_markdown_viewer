"""
We keep compat with the old api (from mdv import main)
"""


def mdv_v1():
    from mdv import markdownviewer

    return markdownviewer


def main(*a, **kw):
    mdv = mdv_v1()
    return mdv.main(*a, **kw)
