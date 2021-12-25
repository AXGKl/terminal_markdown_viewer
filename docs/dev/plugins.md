# Developer Information

    
Subsequently we provide information for developers, who want to understand / change / extend / contribute to functionality of mdv.

## Plugins

Most of the code is organized into swappable plugins, so that mdv's functionality or used libraries
may be modified and or extended.

### Packaged Plugins

mdv ships with the following plugins:

```python lp:python
from mdv.plugins import config
from lcdoc.mkdocs.tools import srclink
P = config.Plugins
def draw_table(cls):
  r = []; add = r.append
  add('| name | module |')
  add('|-|-|')
  for p in sorted([k for k in dir(cls) if not k.startswith('_')]):
    n = getattr(cls, p)
    p = f'[{p}](./plugs/{p}.md)'
    if isinstance(n, str):
        url = srclink(f"src/mdv/plugins/{n}.py",ctx['LP'].config, line=1, title=f'{n}')['url']
        add(f'| {p} | [{n}]({url}) |')
  show('\n'.join(r))
draw_table(config.Plugins)
show('\n\nAction Plugins:  \n\n')
draw_table(config.Plugins.Actions)

```



### Action Plugins

Certain plugins are "action plugins". Those have to have a `run` method, which is called by the
`conf` plugin, depended on how the user invokes "mdv" on the CLI.

Example: User calling `$ mdv foo <arguments>` results in an invocation of `foo.run()` (regarding
handling of all other CLI arguments see the [`conf`](./plugs/conf.md)).

Default Action Plugin, i.e. when the user does no specify any on the CLI, is
[`view`](./plugs/view.md), whoose `run` method outputs the rendering result in the terminal.

!!! note

    There is no interface convention for plugins. They are just modules, which are tried to be
    imported first from the user's config directory (at `~/.config/mdv/plugs`), then from the mdv
    package, if not provided by the user.


### Invocation Sequence

Here 

```bash lp:kroki fn=img/k1
actor User as u
participant mdv.main as mdv
participant mdv.conf as conf
participant mdv.foo as view

u->mdv: $ mdv foo --bar=baz
note over mdv: main() imports "conf" plugin\n(from user or package)
mdv->conf: Calls configure(sys.argv)
note over conf: - Loads config file,\n- parses environ and argv\n- finds wanted action plugin
note over mdv, conf: tools.C (global config) now populated\n(e.g. tools.C["bar"] is "baz").\naction plugin(s) known.
mdv->conf: Calls run()
conf->view: Calls run() on all action plugins
note over view: Uses other plugins,\ne.g. "mdparser", "render".
```


### Plugin Loading

- Plugins are imported by name, at first use. 
- Name points to module wanted. name






### Plugin 

### Plugin Conventions

    , which have to provide
    certain functions, and they are registered by name. Except that "action plugins" (invokable on
    the CLI, default 'view') have to have a `run` method. 


Some plugins are "action plugins" 


### Plugin Loading Mechanics

- The first plugin loaded is `conf`, via mdv's main method:

`lp:show_src delim=mdv_main dir=src eval=always lang=python`

- `conf




Any plugin has a name 
Example: Markdown to html converter.










The plugins mdv provides 'out of the box' are listed in the package's default config file, which the
[conf](./plugs/conf.md) plugin imports:

`lp:show_src delim=default_plugins dir=src eval=always lang=python`


Those plugins are are imported lazily by the [`plugs`](<{config.repo_url}>/tree/master/src/mdv/plugs.py) module,
at first use of `tools.plugins.<some plugin name>`, via a getattr hook:

`lp:show_src delim=plugins_load dir=src eval=always lang=python`

After import `run_hook('post_import', <plugin module>)` is invoked, if that function is present.

!!! note

    There is no interface convention for plugins, they are just modules, registered by name. Except
    that "action plugins" (invokable on the CLI, default 'view') have to have a `run` method. 

The first plugin loaded is `conf`, via the main method:

`lp:show_src delim=mdv_main dir=src eval=always lang=python`

See [here](plugs/conf.md) for more on the `conf` plugin.

!!! hint "IDE Support"

    IDEs cannot resolve getattr based lazy loading of code. To profit from IDE features like "go to
    definition", we use a trick: We import the plugins in the `plugs` module at program start, when
    an env var is set. You don't actually need to set it but
    [LSPs](https://microsoft.github.io/language-server-protocol/) like pyright then find the
    definitions, allthough in reality never imported w/o the env variable being set.


## Action Plugins

Actions are special plugins, with a `run` method. They are loaded (and run is called) based on CLI
entry. Default is action `view`.

## Creating Plugins

It should be straightforward to create new functionality, based on top of mdv's existing functions.

## Overwriting Existing Functionality

Example: you want to use a different md to html renderer.

- Overwrite an existing one with your version and put the file into the your `~/.config/mdv/plugs` folder. 
- Or: Create a *new* file for the same functionality and provide the name to file mapping in your  `~/.config/mdv/config.py: class Plugins`.

### New Functionality

Say you want an `mdv2 foo --bar=baz (...)`

- create a new action module `foo.py` in `plugs`, with a run method.
- It can call also other plugins where names default to module filename w/o extension, if not mapped in `config.py`.  
  They will be imported at first use (via a `__getattr__` hook in `class Plugins`).
- You *can* (but not have to) provide defaults for the cli parameters in `config.py`. 

!!! caution "Flat Name Space"

    The config namespace is flattened into a flat dict. The classes in `config.py` are only to
    organize help output.



