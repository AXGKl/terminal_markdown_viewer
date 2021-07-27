"""_
# Usage:

    mdv [options] [MDFILE]

# Options:
    -A         : no_colors     : Strip all ansi (no colors then)
    -C MODE    : code_hilite   : Sourcecode highlighting mode
    -F FILE    : config_file   : Configfile, alternative to ~/.config/mdv/config.py
    -H         : do_html       : Print html version
    -L         : display_links : Backwards compatible shortcut for '-u i'
    -M DIR     : monitor_dir   : Monitor directory for markdown file changes
    -R         : rm_spaces     : Replace consecutive spaces with a single one (except at code and line endings)
    -S FILE    : css_file      : CSS file, alternative to ~/.config/mdv/user.css
    -T C_THEME : c_theme       : Theme for code highlight. If not set we use THEME
    -X Lexer   : c_def_lexer   : Default lexer name (default python). Set -x to use it always.
    -b TABL    : tab_length    : Set tab_length to sth. different than 4 [default 4]
    -c COLS    : cols          : Fix columns to this (default <your terminal width>)
    -f FROM    : from_txt      : Display FROM given substring of the file
    -h         : help          : Show help
    -i         : theme_info    : Show theme infos with output
    -l         : log_level     : debug, info, warning or error (goes to stderr)
    -m         : monitor_file  : Monitor file for changes and redisplay FROM given substring
    -n NRS     : header_nrs    : Header numbering (default off. Say e.g. -3 or 1- or 1-5)
    -s JSON    : style         : Style dict (e.g.: '{"H1": 124}')
    -t THEME   : theme         : Key within the color ansi_table.json. 'random', 'd or default' and 'all' understood
    -u STYL    : link_style    : Link Style (it=inline table=default, h=hide, i=inline)
    -x         : c_no_guess    : Do not try guess code lexer (guessing is a bit slow)
"""
import sys

# from .plugs import PY3, C, fix_py2_default_encoding, plugins  # isort:skip
from .plugs import plugins  # isort:skip


def main():
    # not sure if we are able to support py2 but this is obligatory in any case:
    # fix_py2_default_encoding() if not PY3 else None
    # imports all plugins starting with "mdv_", plus knows then all *available* files:
    # mdv_conf is a must have plugin, so we have it:
    plugins.conf.configure(argv=list(sys.argv))
    plugins.conf.run()


if __name__ == '__main__':  # pragma: no cover
    # the setup tools version calls directly main, this is for git checkouts:
    main()
