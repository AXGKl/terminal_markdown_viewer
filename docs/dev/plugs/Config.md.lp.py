{'73c02eb6f6524b1bab84ccaa733260d2': {'cmd': '$ cat '
                                             '/home/gk/repos/terminal_markdown_viewer/src/mdv/plugins/config.py',
                                      'res': '# fmt:off\n'
                                             "environ_prefix = 'MDV_'\n"
                                             '\n'
                                             '# :docs:default_plugins\n'
                                             'class Plugins:\n'
                                             '    # functional name = module '
                                             'name (in user or pkg plugins '
                                             'dir)\n'
                                             '    boxes             = '
                                             "'term_css_boxes'\n"
                                             "    color             = 'color'\n"
                                             '    colors_256        = '
                                             "'color_table_256'\n"
                                             '    colors_web        = '
                                             "'color_table_web'\n"
                                             '    conf              = '
                                             "'mdv_conf'\n"
                                             '    log               = '
                                             "'structlog'\n"
                                             '    mdparser          = '
                                             "'pymarkdown'\n"
                                             '    render            = '
                                             "'term_render'\n"
                                             '    style             = '
                                             "'term_css_style'\n"
                                             '    textmaps          = '
                                             "'term_font_textmaps.py'\n"
                                             '    theme             = '
                                             "'theme_base16'\n"
                                             '    tree_analyzer     = '
                                             "'html_beautifulsoup'\n"
                                             '\n'
                                             '    class Actions:\n'
                                             '        colortables= '
                                             "'colortables'\n"
                                             "        view       = 'view'\n"
                                             "        help       = 'help'\n"
                                             '\n'
                                             '# :docs:default_plugins\n'
                                             '\n'
                                             'class Output:\n'
                                             '    html_out = None # when given '
                                             "we write the html here ('-' for "
                                             'stdout)\n'
                                             '    term_out = None # when given '
                                             "we write the ansi here ('-' set "
                                             'as default when run from cli)\n'
                                             '    ruler = None # add a '
                                             'horizontal ruler for terminal '
                                             'output\n'
                                             '    \n'
                                             '\n'
                                             'class Logging:\n'
                                             '    # pip install structlog '
                                             'provides nice dev logging Eats '
                                             'around 0.03s app startup time '
                                             'though.\n'
                                             "    log_level     = 'info'\n"
                                             '\n'
                                             'class Terminal:\n'
                                             '    true_color     = True\n'
                                             '    width          = 0 # 0: '
                                             'auto\n'
                                             '    height         = 0\n'
                                             '    width_default  = 80 # '
                                             'fallback\n'
                                             '    height_default = 24\n'
                                             '\n'
                                             'class Markdown:\n'
                                             '    rm_spaces   = True\n'
                                             '    tab_length  = 4\n'
                                             "    sample_text = '''# "
                                             'H1\\nHello *World!* from '
                                             "mdv!'''\n"
                                             '\n'
                                             '\n'
                                             'class Styling:\n'
                                             '    # those are initialized with '
                                             'display: inline even w/o a '
                                             'stylesheet:\n'
                                             "    inline_tags = ['em', "
                                             "'strong', 'b', 'code', 'del', "
                                             "'super', 'sub']\n"
                                             "    theme = 'theme_base16' \n"
                                             "    css_file   = '' # requires "
                                             'pip install cssutils\n'
                                             '\n'
                                             '    class Variables:\n'
                                             '        class Text:\n'
                                             "            hr_sep        = '─'\n"
                                             "            txt_block_cut = '✂'\n"
                                             "            code_pref     = '| "
                                             "'\n"
                                             "            list_pref     = '- "
                                             "'\n"
                                             "            bquote_pref   = '|'\n"
                                             "            hr_ends       = '◈'\n"
                                             '\n'
                                             '        class Cells:\n'
                                             "            H1     = '1;33'\n"
                                             "            H2     = '1;32'\n"
                                             "            H3     = '1;35'\n"
                                             "            H4     = '1;35'\n"
                                             "            H5     = '1;34'\n"
                                             "            R      = '31'\n"
                                             "            L      = '2;90'\n"
                                             "            BG     = '30'\n"
                                             "            BGL    = '30'\n"
                                             "            D      = ''\n"
                                             "            T      = '36'\n"
                                             "            C      = '3;100;97'\n"
                                             "            EM     = '3;31'\n"
                                             "            STRONG = '1;32;41'\n"
                                             '            CH1, CH2, CH3, CH4, '
                                             'CH5 = H1, H2, H3, H4, H5\n'
                                             '\n'
                                             '        class Admonitions:\n'
                                             "            attention = 'H1'\n"
                                             "            caution   = 'H2'\n"
                                             "            danger    = 'R'\n"
                                             "            dev       = 'H5'\n"
                                             "            hint      = 'H4'\n"
                                             "            note      = 'H3'\n"
                                             "            question  = 'H5'\n"
                                             "            summary   = 'H1'\n"
                                             "            warning   = 'R'\n"
                                             '\n'
                                             '        class Code:\n'
                                             '            def_lexer   = '
                                             "'python'\n"
                                             '            guess_lexer = True\n'
                                             '\n'
                                             '            class Highlight:\n'
                                             "                Comment  = 'L'\n"
                                             "                Error    = 'R'\n"
                                             '                Generic  = '
                                             "'CH2'\n"
                                             '                Keyword  = '
                                             "'CH3'\n"
                                             '                Name     = '
                                             "'CH1'\n"
                                             '                Number   = '
                                             "'CH4'\n"
                                             '                Operator = '
                                             "'CH5'\n"
                                             '                String   = '
                                             "'CH4'\n"
                                             '\n'
                                             '\n'
                                             '    class CSS:\n'
                                             "        BQ         = {'border': "
                                             "'2 solid H1'}\n"
                                             "        UL         = {'padding': "
                                             '2}\n'
                                             "        OL         = {'padding': "
                                             '2}\n'
                                             '\n'
                                             '\n'
                                             '# ansi cols (default):\n'
                                             '# Convention:\n'
                                             '# Numbers are the ansi 256 color '
                                             'codes (those are independent of '
                                             'your terminal theme)\n'
                                             '# Strings: Ansi code as is.\n'
                                             '# Example: 124 rendered '
                                             "identical as '38;5;124' or 'H4' "
                                             'if H4 then is 124\n'
                                             '# The string form allows to set '
                                             'also underlined, bold, (...) if '
                                             'your term supports it.\n'
                                             '# See e.g.: '
                                             'https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences/33206814#33206814\n'
                                             '\n'
                                             '# Semantics:\n'
                                             '# R: Red (warnings), L: low '
                                             'visi, BG: background, BGL: '
                                             'background light, C=code\n'
                                             '# H1 - H5 = the color theme.\n'
                                             '\n'
                                             '\n'
                                             '#     ,  # H1: bold yellow\n'
                                             '#     ,  # bold green\n'
                                             '#     ,  # bold cyan\n'
                                             '#     ,  # bold magenta\n'
                                             '#     ,  # H5 bold blue\n'
                                             '#     ,  # R red\n'
                                             '#     ,  # L dimmed bright black '
                                             '-> rendered as gray usually\n'
                                             '#     ,  # black\n'
                                             '#     ,  # black\n'
                                             "#     '',  # D: document (outer "
                                             'div)\n'
                                             '#     ,  # T(ext) white\n'
                                             '#     ,  # C(ode) italic bright '
                                             'b/w bg and fg\n'
                                             "#     '3;31',  # em italics\n"
                                             "#     '1;32;41',  # bold\n"
                                             "#     {'border': '2 solid H1'},\n"
                                             '#     # {\n'
                                             "#     #     'ansi': '1;32',\n"
                                             "#     #     'border': '1 solid "
                                             "H1',\n"
                                             "#     #     'border-right': '2 "
                                             "dashed H2',\n"
                                             "#     #     'border-left': '3 "
                                             "solid H2',\n"
                                             "#     #     'margin': 1,\n"
                                             "#     #     'padding': 2,\n"
                                             '#     # },\n'
                                             "#     {'border': '2 solid H1'},\n"
                                             "#     {'padding': 2, 'ansi': "
                                             "'H2'},\n"
                                             '# )\n'
                                             '# # normal text color:\n'
                                             "# color = 'T'\n"
                                             '\n'
                                             '# # terminal columns (width). 0 '
                                             '-> autodetect or use from cli\n'
                                             '# col = 0\n'
                                             '\n'
                                             '# # hirarchical indentation by:\n'
                                             "# left_indent = '  '\n"
                                             '\n'
                                             "# link_start = '①'\n"
                                             '# link_start_ord = '
                                             'ord(link_start)\n'
                                             '\n'
                                             "# log_level = 'debug'\n"
                                             '\n'
                                             '# # it: inline table, h: hide, '
                                             'i: inline\n'
                                             "# show_links = 'it'\n"
                                             '\n'
                                             '# tab_length = 4\n'
                                             '\n'
                                             '# # could be given, otherwise '
                                             'read from ansi_tables.json:\n'
                                             '# themes = {}\n'
                                             '\n'
                                             '\n'
                                             '# # sample for the theme roller '
                                             'feature:\n'
                                             "# md_sample = ''\n"
                                             '\n'
                                             '# # dir monitor recursion max:\n'
                                             '# mon_max_files = 1000\n'
                                             '\n'
                                             '# rm_spaces = True\n'
                                             '\n'
                                             "# sample_text = '''\n"
                                             '# # H1\n'
                                             '\n'
                                             '# Hello *World!*\n'
                                             "# '''\n"
                                             '\n'
                                             '# '
                                             '------------------------------------------------------------------ '
                                             'End Config\n'}}