# Developer Notes

## Development Installation

We are using [poetry](https://python-poetry.org/docs/cli/) as build system,
i.e. you need to have the `poetry` command installed.

Then, within the repo say: `poetry install -> poetry shell`. Now you can
develop the sources.

Have a look at `pyproject.toml` regarding project setup and tools.

## Formatting

This is only important for Pull Requests.

- Line Length is 90.
- Please note that we are using a [modified
  version](https://pypi.org/project/axblack/) of `black`, defaulting to single
  quotes(!).   
  `poetry install` will install that `black` version - a dedicated
  virtual env therefore is really required, if you prefer the default version
  of black in your normal work.

## Basic Mechanics

Most of the code is in plugins, which are imported lazily by the
[`plugs`]({{config.repo_url}}src/mdv/plugs.py) module, at first use of
`tools.plugins.<some plugin name>`, via a getattr hook.

!!! hint "IDE Support"  
    To profit from features like definition browsing, we
    import the plugins in the `plugs` module, when an env var is set.
    [LSPs](https://microsoft.github.io/language-server-protocol/) like pyright then
    find the definitions, allthough in reality never imported w/o the env variable.



