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
