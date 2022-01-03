# Plugin `mdparser`: Markdown to HTML

## General Functionality

This plugin, via its `convert` function, wraps the markdown to html library to use. It must support
`convert(md)`, which converts a markdown string and returns html.

Called by: [`view`](./view.md) action plugin. 

## Default Implementation: :srcref:fn=src/mdv/plugins/pymarkdown.py,t=pymarkdown.py

This is just a thin wrapper around the [`markdown`](https://pypi.org/project/Markdown/) library.


### Customizing Extensions

Currently you have to [provide](../plugins.md) your own little version of the plugin, importing the extensions you
want.



## Custom Markdown Parser


If you don't use [`markdown`](https://pypi.org/project/Markdown/) you have anyway total freedom
regarding *how* you convert to html.
