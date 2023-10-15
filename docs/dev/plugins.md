# Developer Information
    
Subsequently we provide information for developers, who want to understand / change / extend / contribute to functionality of mdv.

## Plugins

Most of the code is organized into swappable plugins, so that mdv's functionality or used libraries
may be swapped, modified and or extended.

Also existing plugins might be used as building blocks, to create new applications (see Action Plugins).

### Lookup Table: Packaged Plugins

The plugins mdv already ships with are listed below.

!!! note
    The [config file](./plugs/Config.md) defines, which module is to be imported for which
    functionality.

```python lp:python
from mdv.plugins import config
from lcdoc.mkdocs.tools import srclink
P = config.Plugins
def draw_table(cls, do_config_py=False):
  r = []; add = r.append
  add('| functional name | module name |')
  add('|-|-|')
  for p in sorted([k for k in dir(cls) if not k.startswith('_')]):
    n = getattr(cls, p)
    lnk = f'(./plugs/{p}.md)'
    p = f'[{p}]' + lnk
    if isinstance(n, str):
        url = srclink(f"src/mdv/plugins/{n}.py",ctx['LP'].config, line=1)['url']
        add(f'| {p} | [{n}]({url}) |')
  if do_config_py:
        url = srclink(f"src/mdv/plugins/config.py",ctx['LP'].config, line=1)['url']
        add(f'| (mdv config file) | [config]({url}) |')

  show('\n'.join(r))
show('\n\nAction Plugins:  \n\n')
draw_table(config.Plugins.Actions)
show('\n\nOther Plugins:  \n\n')
draw_table(config.Plugins, do_config_py=True)

```

### Conventions 

There is *no* interface convention for plugins. They are just modules, which are tried to be
imported

- first from the user's config directory (at `~/.config/mdv/plugs`), then, if not found,
- from the mdv package

when a functionality, e.g. logging or markdown parsing, is required from anywhere in the code.

*Which* module is imported, when certain functionality is required, depends on user's config file
and CLI invocation parameters (see below).

### Action Plugins

Those have to have a `run` method, which is called by the `conf` plugin, depended on how the user
invokes "mdv" on the CLI.

Example: User calling `$ mdv foo <parameters>` results in an invocation of `foo.run()`.

!!! note
    Regarding handling of all other CLI arguments see also the [`conf`](./plugs/conf.md).

[`view`](./plugs/view.md) is the **default action plugin** (i.e. when the user does no specify any on the CLI),
whose `run` method outputs the rendering result in the terminal.


### Lazy Plugin Loading

Plugins are are imported lazily by the [`plugs`](<{config.repo_url}>/tree/master/src/mdv/plugs.py) module,
at *first* invocation of `tools.plugins.<functional name>`, i.e. via a `__getattr__` hook:

`lp:show_src delim=plugins_load dir=src eval=always lang=python`

Only conventions:

1. The config file has name "config" and module name "config.py". If not found in user's config dir,
   mdv imports mdv's [default one](./plugs/Config.md).
1. The plugin which configures mdv must have functional name "conf", by default mapped to module
   name `mdv_conf.py`.



### Full Startup Sequence

The first plugin loaded is `conf`, via mdv's main method:

`plugins.conf` triggers the `__getattr__` import hook:

`lp:show_src delim=mdv_main dir=src eval=always lang=python`

!!! note
    The import hook, when the functional plugin name is "conf", will first load the "config.py"
    file, so that it knows the module name of the "conf" plugin.

`conf` then configures mdv and calls the actions plugin(s) wanted by the user.

Example:

- User wants action `view`
- with [`config.py`](./plugs/Config.md) parameter `bar` set to `baz`

I.e. user enters "mdv foo --bar=baz" on the CLI).

This is what happens with the default config machinery:

```bash lp:kroki fn=img/k1
actor User as u
participant "mdv:main" as mdv 
participant plugs.py as plugs
participant "conf plugin\n(dflt: mdv_conf.py)" as conf
participant "view action plugin\n(dflt: view.py)" as view
u->mdv: $ mdv foo --bar=baz
note over mdv: parses argv:\n- adds user conf dir to sys.path\n- registers wanted action plugins
note over mdv: plugins.conf
mdv->plugs: getattr(conf) 
note over plugs: imports config file
note over plugs: imports module mapped\nto functional name "conf"\nfrom user or package dir\n(default: mdv_conf.py)
mdv->conf: Calls configure(sys.argv)
note over conf: - Builds global config dict\n  (tools.C)\n- from config file, environ\nand parsed argv
note over mdv, conf: tools.C (global config) now populated\n(e.g. tools.C["bar"] is "baz").\naction plugin(s) known.
mdv->conf: Calls run()
conf->view: Calls run([kwargs]) on all action plugins
note over view: Uses other plugins,\ne.g. "mdparser", "render".
```

!!! important

    There are some variations regarding how the default conf plugin maps CLI parameters, dependend
    on them being defined in the config file or not. See [conf](./plugs/conf.md) for more on this.


!!! note "Custom Startup Sequence"

    As you can see in the sequence, the `conf` plugin, within its `configure` and `run` methods, is
    responsible for mdv's startup flow. Since conf itself is a plugin as well, you can have your own
    program flow via a custom `mdv_conf.py` (if not remapped to another name in a custom config
    file), within your `$HOME/.config/plugs/` directory.



## IDE Support

IDEs cannot resolve getattr based lazy loading of code, based on module name strings.

To profit from IDE features like "go to definition", we use a trick: We import the plugins in the
`plugs` module at program start, when an env var is set. You don't actually need to set it but
[LSPs](https://microsoft.github.io/language-server-protocol/) like pyright then find the
definitions, although in reality never imported w/o the env variable being set.



## Creating Plugins

It should be straightforward to create new functionality, based on top of mdv's existing ones.

Example: You want to use a different md to html renderer.

- Overwrite an existing one with your version and put the file with same nameinto the your `~/.config/mdv/plugs` folder. 
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



