# Contributing to the Project

## Development Installation

We are using [poetry](https://python-poetry.org/docs/cli/) as build system, i.e. you need to have
the `poetry` command installed.

Then, within the repo say: `poetry install -> poetry shell`. Now you can develop the sources.

Have a look at `pyproject.toml` regarding project setup and tools.

!!! tip make
    In the project root folder there is a little script (`make`), which provides functions
    for repo maintenance, e.g. docs, tests (...). `make -h` lists them.

## Formatting

For Merge Requests, please stick to this formatting:

- We are using a [modified older version](https://pypi.org/project/axblack/) of `black`,
  *defaulting to single quotes(!)*
- `poetry install` will install that `black` version - a dedicated virtual env therefore is really
  required, if you prefer the default version of black in your normal work.
- Line Length is 90.

## Basic Mechanics

### Code Organization: Plugins

Most of the code is in plugins, which are imported lazily by the
[`plugs`](<{config.repo_url}>src/mdv/plugs.py) module, at first use of `tools.plugins.<some plugin
name>`, via a getattr hook.

!!! hint "IDE Support"
    To profit from features like definition browsing, we import the plugins in
    the `plugs` module, when an env var is set.
    [LSPs](https://microsoft.github.io/language-server-protocol/) like pyright then find the
    definitions, allthough in reality never imported w/o the env variable.


There is no interface convention for plugins, they are just modules, registered by name. Except that "action plugins" (invokable on the CLI, default 'view') have to have a `run` method.

### Creating Plugins

It should be straightforward to create new functionality, based on top of mdv's existing functions.

#### Overwriting Existing Functionality

Example: you want to use a different md to html renderer.

- Overwrite an existing one with your version and put the file into the your `~/.config/mdv/plugs` folder. 
- Or: Create a *new* file for the same functionality and provide the name to file mapping in your  `~/.config/mdv/config.py: class Plugins`.

##### New Functionality
Say you want an `mdv2 foo --bar=baz (...)`

- create a new action module `foo.py` in `plugs`, with a run method.
- It can call also other plugins where names default to modul filename w/o extension if not mapped in `config.py`.  
  They will be imported at first use (via a `__getattr__` hook in `class Plugins`).
- You *can* (but not have to) provide defaults for the cli parameters in `config.py`. 

!!! caution "Flat Name Space"
    The config namespace is flattened into a flat dict. The classes in `config.py` are only to
    organize help output.


### Code Organization

## Contributing to Documentation

We use a lot of [literate programming][LP] in the docs, via [this](https://pypi.org/project/docutools/).

This means the docs with literate programming stanzas (`lp` tags after fenced code language names)
have to be *preprocessed*, running the code, generating the output which is displayed by `xterm.js`,
with full ansi support.

!!! caution "Filename Convention: .md.lp"
    Files with literate programming stanzas are named `filename.md.lp`. Those are the primary
    sources and not their corresponding `.md` files.   

    Set you editor accordingly, e.g. vim: `au BufNewFile,BufRead *.lp set filetype=markdown`


!!! hint "doc pre_process"
    In the [make](<{config.repo_url}>/make>) file you find the appropriate commands to run the
    preprocessor, also for preprocess on change.


[LP]: https://en.wikipedia.org/wiki/Literate_programming
