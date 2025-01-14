{'071b6bc18d71660bd72f0ca22fc7aeb0': {'formatted': '\n'
                                                   '=== "Code"\n'
                                                   '\n'
                                                   '    ```python\n'
                                                   '    class '
                                                   'Plugins(DevPlugins):\n'
                                                   '        def '
                                                   '__getattr__(self, '
                                                   'plug_name):\n'
                                                   '            """only called '
                                                   'at a miss. -> ideal to '
                                                   'lazy import"""\n'
                                                   '            # the first '
                                                   "plugin is 'conf', called "
                                                   'in main, populating the '
                                                   'conf dict from config\n'
                                                   '            # file in '
                                                   "user's conf dir or mdv pkg "
                                                   '-> after this we know all '
                                                   'configurable kvs\n'
                                                   '            # plus we know '
                                                   'which action the user '
                                                   'called (default: view), '
                                                   'whichhh will be\n'
                                                   '            if plug_name '
                                                   "== 'conf':\n"
                                                   '                '
                                                   'set_sys_path_and_load_config()\n'
                                                   '            # '
                                                   'FileConfig[0] is from the '
                                                   'config file, listing all '
                                                   'available plugins by '
                                                   'name:\n'
                                                   '            filename = '
                                                   'getattr(FileConfig[0].Plugins, '
                                                   'plug_name, plug_name)\n'
                                                   '            # import it '
                                                   'and run the post_import '
                                                   'hook:\n'
                                                   '            return '
                                                   'load_plugin(plug_name, '
                                                   'filename)\n'
                                                   '    ```\n'
                                                   '\n'
                                                   '=== '
                                                   '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugs.py#L107)"\n'
                                                   '    '
                                                   'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugs.py#L107\n',
                                      'res': '\n'
                                             '=== "Code"\n'
                                             '\n'
                                             '    ```python\n'
                                             '    class Plugins(DevPlugins):\n'
                                             '        def __getattr__(self, '
                                             'plug_name):\n'
                                             '            """only called at a '
                                             'miss. -> ideal to lazy '
                                             'import"""\n'
                                             '            # the first plugin '
                                             "is 'conf', called in main, "
                                             'populating the conf dict from '
                                             'config\n'
                                             "            # file in user's "
                                             'conf dir or mdv pkg -> after '
                                             'this we know all configurable '
                                             'kvs\n'
                                             '            # plus we know which '
                                             'action the user called (default: '
                                             'view), whichhh will be\n'
                                             '            if plug_name == '
                                             "'conf':\n"
                                             '                '
                                             'set_sys_path_and_load_config()\n'
                                             '            # FileConfig[0] is '
                                             'from the config file, listing '
                                             'all available plugins by name:\n'
                                             '            filename = '
                                             'getattr(FileConfig[0].Plugins, '
                                             'plug_name, plug_name)\n'
                                             '            # import it and run '
                                             'the post_import hook:\n'
                                             '            return '
                                             'load_plugin(plug_name, '
                                             'filename)\n'
                                             '    ```\n'
                                             '\n'
                                             '=== '
                                             '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugs.py#L107)"\n'
                                             '    '
                                             'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugs.py#L107\n'},
 '732c541802dffaac825db709b70c8739': {'formatted': '\n'
                                                   '=== "Code"\n'
                                                   '\n'
                                                   '    ```python\n'
                                                   '    class Plugins:\n'
                                                   '    \n'
                                                   '        boxes          = '
                                                   "'term_css_boxes'\n"
                                                   '        color          = '
                                                   "'color'\n"
                                                   '        colors_256     = '
                                                   "'color_table_256'\n"
                                                   '        colors_web     = '
                                                   "'color_table_web'\n"
                                                   '        conf           = '
                                                   "'mdv_conf'\n"
                                                   '        log            = '
                                                   "'structlog'\n"
                                                   '        mdparser       = '
                                                   "'pymarkdown'\n"
                                                   '        render         = '
                                                   "'term_render'\n"
                                                   '        style          = '
                                                   "'term_css_style'\n"
                                                   '        textmaps       = '
                                                   "'term_font_textmaps.py'\n"
                                                   '        theme          = '
                                                   "'theme_base16'\n"
                                                   '        tree_analyzer  = '
                                                   "'html_beautifulsoup'\n"
                                                   '    \n'
                                                   '        class Actions:\n'
                                                   '            colortables= '
                                                   "'colortables'\n"
                                                   '            view       = '
                                                   "'view'\n"
                                                   '            help       = '
                                                   "'help'\n"
                                                   '    ```\n'
                                                   '\n'
                                                   '=== '
                                                   '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/config.py#L5)"\n'
                                                   '    '
                                                   'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/config.py#L5\n',
                                      'res': '\n'
                                             '=== "Code"\n'
                                             '\n'
                                             '    ```python\n'
                                             '    class Plugins:\n'
                                             '    \n'
                                             '        boxes          = '
                                             "'term_css_boxes'\n"
                                             '        color          = '
                                             "'color'\n"
                                             '        colors_256     = '
                                             "'color_table_256'\n"
                                             '        colors_web     = '
                                             "'color_table_web'\n"
                                             '        conf           = '
                                             "'mdv_conf'\n"
                                             '        log            = '
                                             "'structlog'\n"
                                             '        mdparser       = '
                                             "'pymarkdown'\n"
                                             '        render         = '
                                             "'term_render'\n"
                                             '        style          = '
                                             "'term_css_style'\n"
                                             '        textmaps       = '
                                             "'term_font_textmaps.py'\n"
                                             '        theme          = '
                                             "'theme_base16'\n"
                                             '        tree_analyzer  = '
                                             "'html_beautifulsoup'\n"
                                             '    \n'
                                             '        class Actions:\n'
                                             '            colortables= '
                                             "'colortables'\n"
                                             "            view       = 'view'\n"
                                             "            help       = 'help'\n"
                                             '    ```\n'
                                             '\n'
                                             '=== '
                                             '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/config.py#L5)"\n'
                                             '    '
                                             'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/config.py#L5\n'},
 '81b9e14748c13e74449a8be17ce1709d': {'formatted': '\n'
                                                   '=== "Code"\n'
                                                   '\n'
                                                   '    ```python\n'
                                                   '    def main():\n'
                                                   '        # not sure if we '
                                                   'are able to support py2 '
                                                   'but this is obligatory in '
                                                   'any case:\n'
                                                   '        if not PY3:\n'
                                                   '            '
                                                   'fix_py2_default_encoding()\n'
                                                   '        # conf (default: '
                                                   'mdv_conf.py) is a must '
                                                   'have plugin:\n'
                                                   '        # 1. plugins.conf '
                                                   'imports it (getattr hook)\n'
                                                   '        # .configure '
                                                   'populates the globals.C dict '
                                                   'with all values from file, '
                                                   'env, cli\n'
                                                   '        # .run runs all '
                                                   'action functions (default: '
                                                   'view)\n'
                                                   '        '
                                                   'plugins.conf.configure(argv=list(sys.argv)).run()\n'
                                                   '    ```\n'
                                                   '\n'
                                                   '=== '
                                                   '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/cli.py#L8)"\n'
                                                   '    '
                                                   'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/cli.py#L8\n',
                                      'res': '\n'
                                             '=== "Code"\n'
                                             '\n'
                                             '    ```python\n'
                                             '    def main():\n'
                                             '        # not sure if we are '
                                             'able to support py2 but this is '
                                             'obligatory in any case:\n'
                                             '        if not PY3:\n'
                                             '            '
                                             'fix_py2_default_encoding()\n'
                                             '        # conf (default: '
                                             'mdv_conf.py) is a must have '
                                             'plugin:\n'
                                             '        # 1. plugins.conf '
                                             'imports it (getattr hook)\n'
                                             '        # .configure populates '
                                             'the globals.C dict with all values '
                                             'from file, env, cli\n'
                                             '        # .run runs all action '
                                             'functions (default: view)\n'
                                             '        '
                                             'plugins.conf.configure(argv=list(sys.argv)).run()\n'
                                             '    ```\n'
                                             '\n'
                                             '=== '
                                             '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/cli.py#L8)"\n'
                                             '    '
                                             'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/cli.py#L8\n'}}