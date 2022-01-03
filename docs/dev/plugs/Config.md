# Plugin `config`: Declaring Defaults

This is the first plugin imported - the actual config file.

!!! note
    
    You have the full python magic available here but remember that a config file should be
    declarative, allowing introspection - but not loaded with code.

## General Functionality

The config file delivering a set of default config values, which the [conf](./conf.md) plugin will
put into a (flat!) global config dict, `mdv.globals.C`.


## Default Implementation: :srcref:fn=src/mdv/plugins/config.py,t=config.py

The default config file has (together with the default configurator plugin, `mdv_conf.py`), the job
to

- providing all default kvs
- providing validation rules
- providing mappings for those plugins whose plugin name is different than the module name (same
  name not needed to declare - but useful for help output "what's available")


??? "Default Config File Contents"

    `lp:show_file fmt=mk_console fn=$LP_PROJECT_ROOT/src/mdv/plugins/config.py lang=python`


## Custom Config Files

The user may overwrite the kvs of the packaged config file, within his config directory
(`~/.config/mdv/plugs/config.py`).


Check the examples of the [conf](./conf.md) plugin, for further customization possibilites.
