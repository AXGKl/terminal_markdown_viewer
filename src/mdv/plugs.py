"""
Plugin provider

Imports at first use from ~/.config/mdv/plugs when present else from our plugins dir

"""


import importlib
import os
import shutil
import sys
from fnmatch import fnmatch

here = os.path.realpath(__file__).rsplit(os.path.sep, 1)[0]
envget = os.environ.get

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
    (e.g. goto definition works, even w/o the env var set, tested with pyright LSP in vim)

    => While developping set these to the plugins you are working on
    (plus the env var if you want to skip parametrizing which plugins to load)
    """

    from mdv.plugins import (
        mdv_conf,
        structlog,
        color,
        color_table_256,
        color_table_web,
        pymarkdown,
        term_render,
        term_css_style,
        term_css_boxes,
        term_font_textmaps,
        html_beautifulsoup,
        view,
    )

    class DevPlugins(plugins_base):
        # fmt:off
        boxes                       = term_css_boxes
        color                       = color
        colors_256                  = color_table_256
        colors_web                  = color_table_web
        conf                        = mdv_conf
        log                         = structlog
        mdparser                    = pymarkdown
        render                      = term_render
        style                       = term_css_style
        textmaps                    = term_font_textmaps
        tree_analyzer               = html_beautifulsoup
        view                        = view
        # fmt:on


else:

    class DevPlugins(plugins_base):
        pass


class Plugins(DevPlugins):
    def __getattr__(self, plug_name):
        """only called at a miss. -> ideal to lazy import"""
        if plug_name == 'conf':
            set_sys_path_load_config()
        filename = getattr(FileConfig[0].Plugins, plug_name, plug_name)
        return load_plugin(plug_name, filename)


# imported by tools:
plugins = Plugins()
