# Plugin `theme`: Default Theme

## General Functionality

The configurable `theme` module points to this - it is comparable to your `userchrome.css` of your
browser, i.e. responsible for default styles.

Called by: [`term_css_style`](./style.md)

## Default Implementation: :srcref:fn=src/mdv/plugins/theme_base16.py,t=theme_base16.py

Uses the base16 colors, i.e. the colors are following user's general terminal style.

## Custom Implementation

Based on the default implementation.
