# :srcref:fn=src/mdv/plugins/view.py,t=view: Output Generation

This is the default action, i.e. when no action is given mdv's CLI arguments.

It

1. converts the given markdown file to html, using the [`mdparser`](./mdparser.md) plugin 
1. add style attributes to all html tags, using the [`tree_analyzer`](./tree_analyzer.md) plugin
1. renders the html "soup" into ansi terminal sequences, using the [`render`](./render.md) plugin
1. outputs the result



