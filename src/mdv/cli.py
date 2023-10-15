import os
import sys

from mdv.tools import PY3, die, fix_py2_default_encoding, log

from .globals import C, UserConfigDir, UserPlugs, envget

# from .plugs import PY3, C, fix_py2_default_encoding, plugins  # isort:skip
from .plugs import plugins  # isort:skip


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


def highlight(j):
    try:
        from pygments import highlight as hl
        from pygments.lexers import JsonLexer

        t = C.get('pygm_style')
        l = C.get('pygm_linenos', False)
        if t:
            if C.get('true_color'):
                from pygments.formatters import TerminalTrueColorFormatter as tf
            else:
                from pygments.formatters import Terminal256Formatter as tf

            tf = tf(style=t, linenos=l)
        else:
            from pygments.formatters import TerminalFormatter as tf

            tf = tf(linenos=l)
    except Exception:
        log.warning('No pygments - cannot colorize output')
        return j
    return hl(j, JsonLexer(), tf)


def j_ser(itr):
    try:
        return [a for a in itr]
    except:
        return str(itr)


def output(res):
    if not res:
        return
    out = C.get('term_out')
    out = '-' if out is None else out
    if not out:
        return
    if not isinstance(res, str):
        if isinstance(res, bytes):
            res = res.decode('utf-8')
        else:
            import json

            try:
                tty = sys.stdout.isatty()
                res = json.dumps(res, default=j_ser, indent=None if not tty else True)
                if tty:
                    # pretty print
                    res = highlight(res)
            except:
                pass
    if out in {'-', True}:
        print(res)
    else:
        with open(out, 'w') as fd:
            fd.write(res)


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
    res = plugins.conf.run()
    output(res)


# :docs:mdv_main
if __name__ == '__main__':  # pragma: no cover
    # the setup tools version calls directly main, this is for git checkouts:
    main()
