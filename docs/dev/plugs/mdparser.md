# :srcref:fn=src/mdv/plugins/mdparser.py,t=view: Markdown to HTML

This plugin, via its `convert` function, wraps the markdown to html library to use.

Default is the )[`markdown`](https://pypi.org/project/Markdown/ library.


## Customizing the Markdown Extensions to Use

Currently you have to [provide](../plugins.md) your own little version of the plugin, importing the extensions you
want.

!!! note

    If you don't use [`markdown`](https://pypi.org/project/Markdown/) you have anyway total freedom
    regarding *how* you convert to html.
