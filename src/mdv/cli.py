import sys

# from .plugs import PY3, C, fix_py2_default_encoding, plugins  # isort:skip
from .plugs import plugins  # isort:skip
from mdv.tools import fix_py2_default_encoding, PY3


def main():
    # not sure if we are able to support py2 but this is obligatory in any case:
    if not PY3:
        fix_py2_default_encoding()
    # imports all plugins starting with "mdv_", plus knows then all *available* files:
    # mdv_conf is a must have plugin, so we have it:
    plugins.conf.configure(argv=list(sys.argv))
    plugins.conf.run()


if __name__ == '__main__':  # pragma: no cover
    # the setup tools version calls directly main, this is for git checkouts:
    main()
