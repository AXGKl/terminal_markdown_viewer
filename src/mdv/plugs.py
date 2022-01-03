"""
Plugin provider

First module in use, after cli.py

Imports plugins at first use (via a getattr hook), from ~/.config/mdv/plugs when present
else from our plugins dir

"""


import importlib
import os
import sys

from .globals import UserPlugs, here


def run_hook(hook_name, mod):
    try:
        h = mod.hooks[hook_name]
    except:
        return
    h()


def load_plugin(name, filename=None):
    filename = (filename or name).rsplit('.py', 1)[0]
    nm = 'plugs' if filename + '.py' in UserPlugs else 'mdv.plugins'
    mod = importlib.import_module(nm + '.%s' % filename)
    setattr(plugins, name, mod)  # __getattr__ not invoked from now on
    run_hook('post_import', mod)  # if present
    return mod


# ----------------------------------------------------------------------------- Plugins
by_mod_name = {}


class plugins_base:
    _imported_mod_names = set()
    _all = []
    _mod_by_mod_name = by_mod_name.get


if os.environ.get('MDV_DEV'):
    """
    Development Setup, enabling the IDE to resolve plugins.<func> refs.
    (e.g. goto definition works, even w/o the env var set, tested with pyright LSP in vim)

    => While developping, set these to the plugins you are working on
    (plus the env var if you want to skip parametrizing which plugins to load in the
    config file, the getattr hook below won't be called then)
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


def import_all():
    mods = [load_plugin(up) for up in UserPlugs]
    for k in os.listdir(here + '/plugins'):
        if k.endswith('.py') and k not in UserPlugs:
            mods.append(load_plugin(k))
    return mods


# :docs:plugins_load
class Plugins(DevPlugins):
    def __getattr__(self, plug_name):
        """only called at a miss. -> ideal to lazy import"""

        try:
            if plug_name != 'config':  # raises for 'config', preventing loops
                P = plugins.config.Plugins  # will import config the first time
            filename = getattr(P, plug_name)
        except Exception as ex:
            # different config format, no mapping - try the name as given, allowing:
            # the user to just add an action module and call it on the CLI by name:
            filename = plug_name

        # import it and run the post_import hook if present:
        return load_plugin(plug_name, filename)


# :docs:plugins_load

# imported by tools:
plugins = Plugins()


# begin_archive

# # this just imports config.py, from user or pkg, just like any other plugin:
# # we do not yet have mdv_conf.py imported:
# config = load_plugin('config')
# # Now we have name value mappings for plugins, i.e. can import them in
# # Plugins.__getattr__ below:
# FileConfig.append(config)
