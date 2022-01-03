# Plugin `conf`: Configuring mdv

After having loaded the (usually) purely declarative [config](./Config.md) file, this is the first loaded plugin with actual code, imported
in mdv's `main` function.

See also the [full startup sequence](../plugins.md#full-startup-sequence).


## General Functionality

- must support `configure()`, which
    - identifies the action plugin(s) which the user wants to run (e.g. [`view`](./view.md))
    - populates the `globals.C` dict with all keys and values required by the action plugin(s)

- must support `run()` (which usually calls the action plugin's `run` functions)


Both functions are called from mdv's `main` function.


## Default Implementation: :srcref:fn=src/mdv/plugins/mdv_conf.py,t=mdv_conf.py


### The `configure(argv)` Function

mdv_conf populates `globals.C` with values from

- [Config file](./Config.md)
- Environ: The config file delivers the prefix (key: `environ_prefix`) for environment variables. Default: "MDV_". Values set are overwriting defaults.
- CLI: Variables set in the CLI are overwriting those from any other source.

#### Casting

CLI and environ can only deliver strings.

- If those are declared in config file: We cast to the types of the defaults given there
- Otherwise if those can be cast to float or boolean - we do so.


#### Validation

Basic argument validation is supported, see source code of the plugin.


#### CLI Parsing Details

In order to know any change of the user's wanted configuration directory, we have to parse the CLI
args already before 

=== "CLI Argv Parser Implementation"

    Arguments starting with `--`:

    - are config keys
    - `-` within them replaced to `_` (`--foo-bar` becomes `C['foo_bar']`, as does `--foo_bar`)

    Arguments *not* starting with a `--`:

    - Values for key args before 
    - Action plugins functional name
    - Source filenames (if present in FS). Their content is read into `C.src`


=== "Argv Parser Source Code"

    The argv parser of the default conf module works like this:

    `lp:show_src delim=argvparsing dir=src eval=always lang=python`



### The `run()` Function


mdv_conf loads all action plugin and calls their run functions, with arguments according to their signature.

=== "Plugin Lookup and Run Invocation"

    - Plugins with same function and module name do not have to be declared:

        Plugin names identified in the CLI, which are NOT mapped to module names (within `config.py's`
        `Plugin.Actions`) are tried to be loaded by plugin names.

        Example:

        User has `myplug.py` within his user config directory and a default config file.

        `mdv2 myplug --foo=bar` => `mdv_conf` will try import `myplug` then call `myplug.run(foo=bar)`.


    - `run` signature parameters are passed with values from `globals.C` (i.e. from config file,
      env, cli, after configure)


=== "`mdv_conf.run` Source Code"

    `lp:show_src delim=conf_run_function dir=src eval=always lang=python`


### Examples

Say we have an action plugin "do_sth", with a declared and an undeclared parameter in its run function:


```python lp mode=make_file fn=/tmp/mdv_demo1/plugs/do_sth.py fmt=mk_console eval=always
from mdv.globals import C # default config file has e.g. "log_level"

def run(log_level, myarg='sigval'):
    print(C['log_level'], myarg, C.get('myarg'))
```

Here various invocations:

```bash lp fmt=xt_flat eval=always
mdv2 --config-dir=/tmp/mdv_demo1 do_sth # lp: asserts="info sigval None"
mdv2 --config-dir=/tmp/mdv_demo1 do_sth --myarg=clival --log-level=warning # lp: asserts="warning clival clival"
mdv2 --config-dir=/tmp/mdv_demo1 do_sth --undeclared=xxx | true # lp: asserts=['unknown', 'undeclared']
```



## Custom Configuration Systems

Users can supply their *own* configuration and action invocation system, by providing an alternative
`$HOME/.config/mdv/plugs/mdv_conf.py` file (or remap "conf" to another module name than `mdv_conf`).

It should populate the `globals.C` dict with all required key/values in a `configure` function and then call all wanted action
plugins' `run` functions. 

### Examples

Say we have a `config.py` in a completely different format in user dir, .e.g like this:


```python lp  mode=make_file fn=/tmp/mdv_demo/plugs/config.py fmt=mk_console
# ------------------------------------------- mdv configuration
cfg = {'theme': 'blue'}

class Plugins:
    # mapping this config file itself also as the configurator (i.e. the conf plugin)
    conf = 'config' 

# ------------------------------------------ mdv configurator
# being also conf, we need a configure and run method:
from mdv.globals import C
from mdv.plugs import plugins

def configure(argv):
    C.update(cfg)

def run():
    # we have the global config
    print(C)
    # and can use plugins:
    print(plugins.view)

    # here you would parse sys.argv and call action plugins...

```

Invocation produces:

```bash lp fmt=mk_console
mdv2 --config-dir=/tmp/mdv_demo
```

