# Plugin `style`: Per Tag CSS Object

## General Functionality

Provides normalized CSS information for each html tag.

Called by: [`term_render`](./render.md)

## Default Implementation: :srcref:fn=src/mdv/plugins/term_css_style.py,t=term_css_style.py

Works via decorators which calculate the wanted style.

The calculated style is attached to each tag like this:

```python
(Pdb) pp tag
<h1 style="color:red"></h1>
(Pdb) pp tag.style # the style object of the tag
{style of h1}
(Pdb) pp tag.style._ # the attributes of the style are stored in '_'
{'color': '38;5;9', 'display': 'block'}
```

### Stylesheets and Theme

In a `post_import` hook we load theme and, if given, a `.css` file, which we parse into a `rules`
array. This contains the default style rules.



## Custom Implementation

Would have to provide the same API. Extensions for further CSS attributes via inheritance.
