# Action Plugin `help`: Ansi Color Sequence Lookup

## General Functionality

Present mdv2 help, based on the default [config](./Config.md) format.

!!! caution

    If you use another config format you must customize also the help plugin.

Called by: [`conf.run()`](./conf.md)


## Default Implementation: :srcref:fn=src/mdv/plugins/help.py,t=view.py

```bash lp:bash fmt=xt_flat
mdv2 -h
```


## Customizing the Output

Use any other help viewer.
