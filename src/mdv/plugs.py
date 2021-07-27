import importlib
import os
import shutil
import sys
from fnmatch import fnmatch

here = os.path.realpath(__file__).rsplit(os.path.sep, 1)[0]
envget = os.environ.get
# ---------------------------------------------------------------------------- Packages
# _pkgs = {}


# def delayed_import(pkg, die=True):
#     p = _pkgs.get(pkg)
#     if not p:
#         try:
#             p = _pkgs[pkg] = importlib.import_module(pkg, pkg)
#         except Exception as ex:
#             if die:
#                 raise
#             return None
#     return p


# _plugins = {'usr': [], 'sys': []}


# def find_plugins(into, search_dir):
#     # sys.path.insert(0, d.rsplit('/', 1)[0])
#     into.extend(sorted([k[:-3] for k in os.listdir(search_dir) if k.endswith('.py')]))


# def imp_plugin(mod_name):
#     if not mod_name in plugins._imported_mod_names:
#         mod = importlib.import_module('mdv.plugins.' + mod_name)
#         setattr(plugins, mod.plugin, mod_name)
#         plugins._imported_mod_names.add(mod_name)
#     else:
#         mod = dev_plugins._mod_by_mod_name(mod_name)
#     return mod

FileConfig = []
UserPlugs = set()


def run_hook(hook_name, mod):
    try:
        h = mod.hooks[hook_name]
    except:
        return
    h()


def load_plugin(name, filename=None):
    filename = filename or name
    nm = 'plugs' if filename + '.py' in UserPlugs else 'mdv.plugins'
    mod = importlib.import_module(nm + '.%s' % filename)
    setattr(plugins, name, mod)
    run_hook('post_import', mod)
    return mod


def set_sys_path_load_config():
    d_usr = envget('HOME', '') + '/.config/mdv'
    if os.path.exists(d_usr + '/plugs'):
        sys.path.insert(0, d_usr)
        UserPlugs.update(set(os.listdir(d_usr + '/plugs')))
    config = load_plugin('config')
    FileConfig.append(config)


# ----------------------------------------------------------------------------- Plugins
by_mod_name = {}


class plugins_base:
    _imported_mod_names = set()
    _all = []
    _mod_by_mod_name = by_mod_name.get


if os.environ.get('MDV_DEV'):
    """
    Development Setup, enabling the IDE to resolve tools.plugins.<func> refs.
    (goto definition works, even w/o the env var set, tested with pyright LSP in vim)

    => While developping set these to the plugins you are working on
    (plus the env var if you want to skip parametrizing which plugins to load)
    """

    from mdv.plugins import (
        build_beautifulsoup,
        mdv_conf,
        mdv_log,
        parse_pymarkdown,
        render_ansi,
        render_textmaps,
        view_style,
        view_ansi_color,
        view_ansi_true_color_codes as ctrue,
        view_ansi_16_color_codes as c16,
    )

    class dev_plugins(plugins_base):

        # fmt:off
        conf                = mdv_conf
        log                 = mdv_log
        style               = view_style
        mdparser            = parse_pymarkdown
        tree_analyzer       = build_beautifulsoup
        render              = render_ansi
        color               = view_ansi_color
        color_codes         = [c16, ctrue]
        textmaps            = render_textmaps
        # fmt:on

    def register_dev_mods():
        b = dev_plugins
        for mods in [getattr(b, n) for n in dir(b) if n[0] != '_']:
            mods = mods if isinstance(mods, list) else [mods]
            for mod in mods:
                mod_name = mod.__file__.rsplit('/', 1)[1].split('.py')[0]
                by_mod_name[mod_name] = mod
                b._imported_mod_names.add(mod_name)

    register_dev_mods()
else:

    class dev_plugins(plugins_base):
        pass


class Plugins(dev_plugins):
    def __getattr__(self, plug_name):
        """only called at a miss. -> ideal to lazy import"""
        if plug_name == 'conf':
            set_sys_path_load_config()
        filename = getattr(FileConfig[0].Plugins, plug_name, plug_name)
        return load_plugin(plug_name, filename)


plugins = Plugins()
