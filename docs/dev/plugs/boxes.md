# Plugin `boxes`: Renders Borders

## General Functionality

Takes care of handing the css 'border' attribute.

Called by: [`style`](./style.md)

## Default Implementation: :srcref:fn=src/mdv/plugins/boxes.py,t=boxes.py

This plugin will pick unicode box drawing characters, dependent on border width and style.


## Custom Renderer

Will probably want to import the default and adapt certain characters.
