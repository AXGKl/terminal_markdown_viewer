# Action Plugin `view`: HTML/Markdown to Printed Output

## General Functionality

The view action turns source (`globals.C['src']`) into printed output.

Called by: [`conf.run()`](./conf.md)


## Default Implementation: :srcref:fn=src/mdv/plugins/view.py,t=view.py

`view` is the default action plugin, orchestrating the output of markdown, using various subordinate
plugins.

### General Flow (Plugins Called)

```bash lp:kroki fn=img/viewflow
start
:view.run(src);
:html=mdparser.convert(src);
:dom=tree_analyzer.walk_tree(html);
:rows=render.visualize(dom);
:print(rows);
stop
```


=== "Call Flow Diagram"

    - This is a demo flow, where we call `mdv2 --src="Hello World"`, illustrating how `view` is calling
    the various subordinate plugins.
    - Not shown is the `conf` plugin.
    - Plugins are listed by their module name. A lookup table is [here](../plugins.md).


=== "Detailed Call Flow"

    ```bash
    mdv2 --src="Hello World"
    ```
    

    ```python lp:python cfl
    import mdv
    from mdv import cli
    from mdv.plugs import plugins
    import sys

    a = ['', '--src="Hello World"']
    def demo():
        r = cli.main(a)

    plugins.conf.configure(a)
    l = mdv.plugs.import_all()
    l.remove(mdv.plugs.plugins.mdv_conf)
    show('call_flow', call=demo, trace=l)
    ```




## Customizing the Output

Done by configuring the different plugins used by view.
