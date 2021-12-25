import sys

# from .plugs import PY3, C, fix_py2_default_encoding, plugins  # isort:skip
from .plugs import plugins  # isort:skip
from mdv.tools import fix_py2_default_encoding, PY3

# :docs:mdv_main
def main():
    # not sure if we are able to support py2 but this is obligatory in any case:
    if not PY3:
        fix_py2_default_encoding()
    # conf (default: mdv_conf.py) is a must have plugin:
    # 1. plugins.conf imports it (getattr hook)
    # .configure populates the tools.C dict with all values from file, env, cli
    # .run runs all action functions (default: view)
    plugins.conf.configure(argv=list(sys.argv)).run()


# :docs:mdv_main

if __name__ == '__main__':  # pragma: no cover
    # the setup tools version calls directly main, this is for git checkouts:
    main()
