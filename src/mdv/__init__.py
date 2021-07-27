"""
This is just for compat with the v1 API
"""

def main(*a, **kw):
    from mdv.v1 import markdownviewer

    return markdownviewer.main(*a, **kw)


class markdownviewer:
    def clean_ansi(s):
        from mdv.v1 import markdownviewer
        return markdownviewer.clean_ansi(s)

