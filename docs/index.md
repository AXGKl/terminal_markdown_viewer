# Terminal Markdown / HTML Viewer

[![Build Status][travis_img]][travis]
<a href='https://coveralls.io/github/axiros/terminal_markdown_viewer?branch=master'>
<img src='https://coveralls.io/repos/github/axiros/terminal_markdown_viewer/badge.svg?branch=master' alt='Coverage Status' /></a>
[![PyPI version](https://badge.fury.io/py/mdv.svg)](https://badge.fury.io/py/mdv)
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

!!! note "Version 2"  
    This is version 2 of `mdv`, available on the CLI as `mdv2`.
    v2 is a complete rewrite, offering a lot of new features. Version 1 is still included and available still via `mdv` though, in order to not break existing tools.  
    For version 1 documentation head over [here](v1).

## Installation

```bash
# within your conda/virtual env of choice:
pip install mdv
mdv2 -h
```

### Version 1

Version 1 also contained in the package, unchanged:

```
mdv -h
```
Throughout this documentation, except the [page](./v1/) about version 1, we refer to the new
version with "mdv".

### Windows

Additional install:

```bash
pip install colorama # provides ANSI escape color mappings
```

### Docker

A Dockerfile is in the assets directory of the repo.

### Development Installation
See [here](dev).




[travis]: https://travis-ci.org/axiros/terminal_markdown_viewer
[travis_img]: https://travis-ci.org/axiros/terminal_markdown_viewer.svg?branch=master
