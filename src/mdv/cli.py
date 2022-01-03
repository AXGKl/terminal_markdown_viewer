import sys, os

# from .plugs import PY3, C, fix_py2_default_encoding, plugins  # isort:skip
from .plugs import plugins  # isort:skip
from .globals import UserConfigDir, envget, UserPlugs
from mdv.tools import fix_py2_default_encoding, PY3, cast, read_file, die


def sys_path_add_user_conf_dir(argv):
    a, cli_cd = argv, None
    if len(a) > 1 and a[1].startswith('--config'):
        if '=' in a[1]:
            k, v = a[1].split('=', 1)
        elif len(a) < 3:
            return die('Require value', arg=a[1])
        else:
            k, v = a[1], a[2]
        if k.replace('-', '_') == '__config_dir':
            cli_cd = UserConfigDir[0] = v
    e = envget
    d_usr = cli_cd or e('CONFIG_DIR') or (e('HOME', '') + '/.config/mdv')
    if os.path.exists(d_usr + '/plugs'):
        sys.path.insert(0, d_usr)
        UserPlugs.update(set(os.listdir(d_usr + '/plugs')))


# :docs:mdv_main
def main(argv=None):
    argv = argv or list(sys.argv)
    # not sure if we are able to support py2 but this is obligatory in any case:
    if not PY3:
        fix_py2_default_encoding()
    sys_path_add_user_conf_dir(argv)
    # conf (default: mdv_conf.py) is a must have plugin:
    # 1. plugins.conf imports it (getattr hook)
    # .configure populates the tools.C dict with all values from file, env, cli
    # .run runs all action functions (default: view)
    plugins.conf.configure(argv=argv)
    plugins.conf.run()


# :docs:mdv_main
if __name__ == '__main__':  # pragma: no cover
    # the setup tools version calls directly main, this is for git checkouts:
    main()
