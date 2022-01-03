# Plugin `render`: DOM to Output

## General Functionality

The `visualize` function of the render plugin turns a DOM into side effect ready output like
`print`.

Called by: [`view`](./view.md) action plugin. 

## Default Implementation: :srcref:fn=src/mdv/plugins/term_render.py,t=term_render.py

Turns the DOM into ANSI escape sequences ready for terminal output, e.g. via print, by the
[`view`](./view.md) action plugin.



## Custom Renderer

Other formats like pdf could be called by other action plugins.
