# fmt:off
environ_prefix = 'MDV_'

class Plugins:

    boxes          = 'term_css_boxes'
    color          = 'color'
    colors_256     = 'color_table_256'
    colors_web     = 'color_table_web'
    conf           = 'mdv_conf'
    log            = 'structlog'
    mdparser       = 'pymarkdown'
    render         = 'term_render'
    style          = 'term_css_style'
    textmaps       = 'term_font_textmaps.py'
    theme          = 'theme_base16'
    tree_analyzer  = 'html_beautifulsoup'

    class Actions:
        colortables= 'colortables'
        view       = 'view'
        help       = 'help'

class Output:
    html_out = None # when given we write the html here ('-' for stdout)
    term_out = None # when given we write the ansi here ('-' set as default when run from cli)
    ruler = None # add a horizontal ruler for terminal output
    

class Logging:
    # pip install structlog provides nice dev logging Eats around 0.03s app startup time though.
    log_level     = 'info'

class Terminal:
    true_color     = True
    width          = 0 # 0: auto
    height         = 0
    width_default  = 80 # fallback
    height_default = 24

class Markdown:
    rm_spaces   = True
    tab_length  = 4
    sample_text = '''# H1\nHello *World!* from mdv!'''


class Styling:
    # those are initialized with display: inline even w/o a stylesheet:
    inline_tags = ['em', 'strong', 'b', 'code', 'del', 'super', 'sub']
    theme = 'theme_base16' 
    css_file   = '' # requires pip install cssutils

    class Variables:
        class Text:
            hr_sep        = '─'
            txt_block_cut = '✂'
            code_pref     = '| '
            list_pref     = '- '
            bquote_pref   = '|'
            hr_ends       = '◈'

        class Cells:
            H1     = '1;33'
            H2     = '1;32'
            H3     = '1;35'
            H4     = '1;35'
            H5     = '1;34'
            R      = '31'
            L      = '2;90'
            BG     = '30'
            BGL    = '30'
            D      = ''
            T      = '36'
            C      = '3;100;97'
            EM     = '3;31'
            STRONG = '1;32;41'
            CH1, CH2, CH3, CH4, CH5 = H1, H2, H3, H4, H5

        class Admonitions:
            attention = 'H1'
            caution   = 'H2'
            danger    = 'R'
            dev       = 'H5'
            hint      = 'H4'
            note      = 'H3'
            question  = 'H5'
            summary   = 'H1'
            warning   = 'R'

        class Code:
            def_lexer   = 'python'
            guess_lexer = True

            class Highlight:
                Comment  = 'L'
                Error    = 'R'
                Generic  = 'CH2'
                Keyword  = 'CH3'
                Name     = 'CH1'
                Number   = 'CH4'
                Operator = 'CH5'
                String   = 'CH4'


    class CSS:
        BQ         = {'border': '2 solid H1'}
        UL         = {'padding': 2}
        OL         = {'padding': 2}


# ansi cols (default):
# Convention:
# Numbers are the ansi 256 color codes (those are independent of your terminal theme)
# Strings: Ansi code as is.
# Example: 124 rendered identical as '38;5;124' or 'H4' if H4 then is 124
# The string form allows to set also underlined, bold, (...) if your term supports it.
# See e.g.: https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences/33206814#33206814

# Semantics:
# R: Red (warnings), L: low visi, BG: background, BGL: background light, C=code
# H1 - H5 = the color theme.


#     ,  # H1: bold yellow
#     ,  # bold green
#     ,  # bold cyan
#     ,  # bold magenta
#     ,  # H5 bold blue
#     ,  # R red
#     ,  # L dimmed bright black -> rendered as gray usually
#     ,  # black
#     ,  # black
#     '',  # D: document (outer div)
#     ,  # T(ext) white
#     ,  # C(ode) italic bright b/w bg and fg
#     '3;31',  # em italics
#     '1;32;41',  # bold
#     {'border': '2 solid H1'},
#     # {
#     #     'ansi': '1;32',
#     #     'border': '1 solid H1',
#     #     'border-right': '2 dashed H2',
#     #     'border-left': '3 solid H2',
#     #     'margin': 1,
#     #     'padding': 2,
#     # },
#     {'border': '2 solid H1'},
#     {'padding': 2, 'ansi': 'H2'},
# )
# # normal text color:
# color = 'T'

# # terminal columns (width). 0 -> autodetect or use from cli
# col = 0

# # hirarchical indentation by:
# left_indent = '  '

# link_start = '①'
# link_start_ord = ord(link_start)

# log_level = 'debug'

# # it: inline table, h: hide, i: inline
# show_links = 'it'

# tab_length = 4

# # could be given, otherwise read from ansi_tables.json:
# themes = {}


# # sample for the theme roller feature:
# md_sample = ''

# # dir monitor recursion max:
# mon_max_files = 1000

# rm_spaces = True

# sample_text = '''
# # H1

# Hello *World!*
# '''

# ------------------------------------------------------------------ End Config
