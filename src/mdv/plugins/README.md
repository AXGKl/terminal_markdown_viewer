# MDV2 Plugins

These modules are loaded since their names are given in `config.py` Plugins.

The handle all kinds of tasks in the rendering process.

## Customization

1. Supply your own module with same name in an `~/.config/mdv/plugs` folder. Those will have import precedence. Naturally you can import there our modules and overwrite only parts.
2. Or: Supply differently named modules in `~/.config/mdv/plugs` - and tell mdv2 to use them, in a custom `~/.config/mdv/plugs/config.py`.
