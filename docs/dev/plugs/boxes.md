# Plugin `color`: Renders Borders

## General Functionality

Takes care of handing the css 'border' attribute.

Called by: [`style`](./term_css_style.md)

## Default Implementation: :srcref:fn=src/mdv/plugins/term_css_color.py,t=color.py

This plugin will pick unicode box drawing characters, dependent on border width and style.


## Custom Renderer

Will probably want to import the default and adapt certain characters.
