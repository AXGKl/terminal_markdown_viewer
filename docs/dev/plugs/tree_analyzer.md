# Plugin `tree_analyzer`: Build a DOM

## General Functionality

This plugin, via its `walk_tree(html)` function, builds a document object model with API from the
html. It's result is typically used by a renderer.

Called by: [`view`](./view.md) action plugin. 

## Default Implementation: :srcref:fn=src/mdv/plugins/html_beautifulsoup.py,t=html_beautifulsoup

Python's standard weapon to parse HTML is [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/).

We also include [SoupSieve](https://facelessuser.github.io/soupsieve/), for CSS selectors.


## Custom Tree Analyzer

Must support all API calls of the subsequent plugins turning the tree into side effects.
