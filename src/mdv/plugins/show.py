"""Outputs various tables"""

from mdv.globals import CLI, C
from mdv.plugs import plugins


# -------------------------------------------------------------------------------- lists
def css_rules(match='', **kw):
    """CSS Rules from theme and css file given"""
    match = match.lower()
    h = plugins.tree_analyzer
    h.walk_tree('<html><body>hi</body></html>')
    return [a for a in plugins.style.rules if match in str(a).lower()]


def dom(**kw):
    """The dom as nested structure"""
    breakpoint()  # FIXME BREAKPOINT


# ------------------------------------------------------------------------------ control
help = lambda: 'Available tables: %s' % ', '.join(lists.keys())


def run(**kw):
    what = CLI.actions.pop() if CLI.actions else None

    if what == 'show' or what not in lists:
        return help()
    return lists[what](**kw)


lists = {'css-rules': css_rules, 'dom': dom}
