# :srcref:fn=src/mdv/plugins/mdv_conf.py,t=conf: Configuring mdv

This is the first loaded plugin, imported in mdv's `main` function, which

1. first imports the "conf" plugin (by default mapping to the `mdv_conf.py` module, if not in user's
   `$HOME/.config/mdv/plugs` dir).
1. then calls `configure` on it, which populates the `tools.C` dict with all values from config
   file, env, cli
1. then calls its `run` functions, where all action functions are invoked (by default, if no action
   is given on the CLI, the `view` plugins' `run` function), e.g. `view.run()` is called here,
   producing output.

## Global Configuration Holder: `tools.C` 

- Populated by the conf plugin from

    - Config file
    - Environ
    - CLI

so that all plugins have their config via `tools.C[<key>]` lookups.

Also finds available actions for the CLI. Default is the [`view`](./view.md) action plugin.

When all wanted actions are known, their `run` functions are called, consecutively.

## Custom Configuration Systems

Users can supply their own configuration and action invocation system, by providing an alternative
`$HOME/.config/mdv/plugs/conf.py` file. It should populate the `tools.C` dict with all required
key/values and then call an actual action functions. 



