{'153193a874494e022b77446a66364bea': {'cmd': '$ cat '
                                             '/tmp/mdv_demo1/plugs/do_sth.py',
                                      'res': 'from mdv.globals import C # '
                                             'default config file has e.g. '
                                             '"log_level"\n'
                                             '\n'
                                             'def run(log_level, '
                                             "myarg='sigval'):\n"
                                             "    print(C['log_level'], myarg, "
                                             "C.get('myarg'))"},
 '464bfec53efdd08ea062f03605cab5ca': {'formatted': '\n'
                                                   '=== "Code"\n'
                                                   '\n'
                                                   '    ```python\n'
                                                   '    def from_cli(into, '
                                                   'argv):\n'
                                                   '        """Parsing argv, '
                                                   'into a global dict (CLI)\n'
                                                   '    \n'
                                                   '        Have to do this '
                                                   'early, before any conf, in '
                                                   'order to get custom '
                                                   'config_dir\n'
                                                   '        \n'
                                                   '        \n'
                                                   '        Mech:\n'
                                                   '        - When starting '
                                                   'with "--" => it\'s a kv => '
                                                   "value is after '=' or next "
                                                   "arg, w/o an '='\n"
                                                   '        - values are '
                                                   'obligatory\n'
                                                   '        - shortnames not '
                                                   'yet supported\n'
                                                   '        - When a filename, '
                                                   'the content is read into '
                                                   "'src' key\n"
                                                   '        - Otherwise it is '
                                                   'considered an action\n'
                                                   '        """\n'
                                                   '    \n'
                                                   '        cast = tools.cast\n'
                                                   '        actions = '
                                                   'CLI.actions\n'
                                                   '        not_conf_args = '
                                                   'CLI.not_conf_args\n'
                                                   '        # into will later '
                                                   'update tools.C dict (in '
                                                   'conf, def configure)\n'
                                                   '        args = argv[1:]\n'
                                                   '        while args:\n'
                                                   '            a = '
                                                   'args.pop(0)\n'
                                                   '            if a[:2] == '
                                                   "'--':\n"
                                                   '                a = a[2:]\n'
                                                   "                if '=' in "
                                                   'a:\n'
                                                   '                    a, v = '
                                                   "a.split('=', 1)\n"
                                                   '                else:\n'
                                                   '                    v = '
                                                   'args.pop(0) if args else '
                                                   "'true'\n"
                                                   '                a = '
                                                   "a.replace('-', '_')\n"
                                                   '                if not a '
                                                   'in into:\n'
                                                   '                    b = '
                                                   'simple_cast(v)\n'
                                                   '                    '
                                                   'not_conf_args[a] = b\n'
                                                   '                else:\n'
                                                   '                    b = '
                                                   'cast(a, v, into)\n'
                                                   '                into[a] = '
                                                   'b\n'
                                                   '                if b is '
                                                   'True or b is False:\n'
                                                   '                    '
                                                   'args.insert(0, v)\n'
                                                   '            elif a == '
                                                   "'-':\n"
                                                   '                '
                                                   "into['src'] = "
                                                   'sys.stdin.read()\n'
                                                   '            # elif '
                                                   'into.get(a) and '
                                                   'getattr(actions(), a, '
                                                   'None):\n'
                                                   '            #     '
                                                   'cli_actions.append(a)\n'
                                                   '            # elif '
                                                   'os.path.exists(a):\n'
                                                   '            #     '
                                                   "into['src'] = "
                                                   'tools.read_file(a)\n'
                                                   '            # else:\n'
                                                   '            #     '
                                                   "into['src'] = a\n"
                                                   '            elif '
                                                   'os.path.exists(a):\n'
                                                   '                '
                                                   "into['src'] = "
                                                   'tools.read_file(a)\n'
                                                   '            else:\n'
                                                   '                # '
                                                   'considered an action '
                                                   'plugin name:\n'
                                                   '                '
                                                   'actions.append(a)\n'
                                                   '        '
                                                   "not_conf_args.pop('config_dir', "
                                                   '0)\n'
                                                   '        '
                                                   "not_conf_args.pop('src', "
                                                   '0)\n'
                                                   '    ```\n'
                                                   '\n'
                                                   '=== '
                                                   '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L72)"\n'
                                                   '    '
                                                   'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L72\n',
                                      'res': '\n'
                                             '=== "Code"\n'
                                             '\n'
                                             '    ```python\n'
                                             '    def from_cli(into, argv):\n'
                                             '        """Parsing argv, into a '
                                             'global dict (CLI)\n'
                                             '    \n'
                                             '        Have to do this early, '
                                             'before any conf, in order to get '
                                             'custom config_dir\n'
                                             '        \n'
                                             '        \n'
                                             '        Mech:\n'
                                             '        - When starting with '
                                             '"--" => it\'s a kv => value is '
                                             "after '=' or next arg, w/o an "
                                             "'='\n"
                                             '        - values are obligatory\n'
                                             '        - shortnames not yet '
                                             'supported\n'
                                             '        - When a filename, the '
                                             "content is read into 'src' key\n"
                                             '        - Otherwise it is '
                                             'considered an action\n'
                                             '        """\n'
                                             '    \n'
                                             '        cast = tools.cast\n'
                                             '        actions = CLI.actions\n'
                                             '        not_conf_args = '
                                             'CLI.not_conf_args\n'
                                             '        # into will later update '
                                             'tools.C dict (in conf, def '
                                             'configure)\n'
                                             '        args = argv[1:]\n'
                                             '        while args:\n'
                                             '            a = args.pop(0)\n'
                                             "            if a[:2] == '--':\n"
                                             '                a = a[2:]\n'
                                             "                if '=' in a:\n"
                                             '                    a, v = '
                                             "a.split('=', 1)\n"
                                             '                else:\n'
                                             '                    v = '
                                             "args.pop(0) if args else 'true'\n"
                                             '                a = '
                                             "a.replace('-', '_')\n"
                                             '                if not a in '
                                             'into:\n'
                                             '                    b = '
                                             'simple_cast(v)\n'
                                             '                    '
                                             'not_conf_args[a] = b\n'
                                             '                else:\n'
                                             '                    b = cast(a, '
                                             'v, into)\n'
                                             '                into[a] = b\n'
                                             '                if b is True or '
                                             'b is False:\n'
                                             '                    '
                                             'args.insert(0, v)\n'
                                             "            elif a == '-':\n"
                                             "                into['src'] = "
                                             'sys.stdin.read()\n'
                                             '            # elif into.get(a) '
                                             'and getattr(actions(), a, '
                                             'None):\n'
                                             '            #     '
                                             'cli_actions.append(a)\n'
                                             '            # elif '
                                             'os.path.exists(a):\n'
                                             "            #     into['src'] = "
                                             'tools.read_file(a)\n'
                                             '            # else:\n'
                                             "            #     into['src'] = "
                                             'a\n'
                                             '            elif '
                                             'os.path.exists(a):\n'
                                             "                into['src'] = "
                                             'tools.read_file(a)\n'
                                             '            else:\n'
                                             '                # considered an '
                                             'action plugin name:\n'
                                             '                '
                                             'actions.append(a)\n'
                                             '        '
                                             "not_conf_args.pop('config_dir', "
                                             '0)\n'
                                             "        not_conf_args.pop('src', "
                                             '0)\n'
                                             '    ```\n'
                                             '\n'
                                             '=== '
                                             '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L72)"\n'
                                             '    '
                                             'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L72\n'},
 '534f8aaa4e2aae39a59bf1abb2bed26b': [{'cmd': 'mdv2 '
                                              '--config-dir=/tmp/mdv_demo1 '
                                              'do_sth',
                                       'res': '$ mdv2 '
                                              '--config-dir=/tmp/mdv_demo1 '
                                              'do_sth\n'
                                              'info sigval None'},
                                      {'cmd': 'mdv2 '
                                              '--config-dir=/tmp/mdv_demo1 '
                                              'do_sth --myarg=clival '
                                              '--log-level=warning',
                                       'res': '$ mdv2 '
                                              '--config-dir=/tmp/mdv_demo1 '
                                              'do_sth --myarg=clival '
                                              '--log-level=warning\n'
                                              'warning clival clival'},
                                      {'cmd': 'mdv2 '
                                              '--config-dir=/tmp/mdv_demo1 '
                                              'do_sth --undeclared=xxx | true',
                                       'res': '$ mdv2 '
                                              '--config-dir=/tmp/mdv_demo1 '
                                              'do_sth --undeclared=xxx | true\n'
                                              '\x1b[2m0\x1b[0m '
                                              '[\x1b[31m\x1b[1merror    '
                                              '\x1b[0m] \x1b[1mUnknown '
                                              'parameters            \x1b[0m '
                                              '\x1b[36munknown\x1b[0m=\x1b[35mundeclared\x1b[0m'}],
 '92d83ac5da6acf2dcd5f27794d72d4a6': {'formatted': '\n'
                                                   '=== "Code"\n'
                                                   '\n'
                                                   '    ```python\n'
                                                   '    def run():\n'
                                                   '        actions = '
                                                   'tools.CLI.actions\n'
                                                   '        not_conf_args = '
                                                   'tools.CLI.not_conf_args\n'
                                                   '        C = tools.C\n'
                                                   '        for a in actions:\n'
                                                   '            try:\n'
                                                   '                p = '
                                                   'getattr(plugins, a)\n'
                                                   '            except '
                                                   'ModuleNotFoundError:\n'
                                                   '                return '
                                                   'tools.die(err.is_no_plugin, '
                                                   'argument=a)\n'
                                                   '            run = '
                                                   "getattr(p, 'run', None)\n"
                                                   '            if run == '
                                                   'None:\n'
                                                   '                return '
                                                   'tools.die(err.is_no_valid_action, '
                                                   'action=a)\n'
                                                   '            # func args '
                                                   'not in config? Potentially '
                                                   'typos:\n'
                                                   '            # we raise on '
                                                   'those, if the sig has no '
                                                   'kw args, else we pass them '
                                                   'into run:\n'
                                                   '            fa = '
                                                   'not_conf_args\n'
                                                   '            if fa:\n'
                                                   '                for k, v '
                                                   'in fa.items():\n'
                                                   '                    fa[k] '
                                                   '= simple_cast(v)\n'
                                                   '            s = '
                                                   'getargspec(run)\n'
                                                   '            kw = {}\n'
                                                   '            for a in '
                                                   's.args:\n'
                                                   '                v = '
                                                   'fa.pop(a, C.get(a))\n'
                                                   '                if v is '
                                                   'not None:\n'
                                                   '                    kw[a] '
                                                   '= v\n'
                                                   '            if '
                                                   's.keywords:\n'
                                                   '                '
                                                   'kw.update(fa)\n'
                                                   '            else:\n'
                                                   '                if fa:\n'
                                                   '                    '
                                                   'tools.die(err.unknown_parameters, '
                                                   "unknown=', '.join([k for k "
                                                   'in fa]))\n'
                                                   '            '
                                                   'ActionResults[a] = '
                                                   'run(**kw)\n'
                                                   '    ```\n'
                                                   '\n'
                                                   '=== '
                                                   '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L176)"\n'
                                                   '    '
                                                   'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L176\n',
                                      'res': '\n'
                                             '=== "Code"\n'
                                             '\n'
                                             '    ```python\n'
                                             '    def run():\n'
                                             '        actions = '
                                             'tools.CLI.actions\n'
                                             '        not_conf_args = '
                                             'tools.CLI.not_conf_args\n'
                                             '        C = tools.C\n'
                                             '        for a in actions:\n'
                                             '            try:\n'
                                             '                p = '
                                             'getattr(plugins, a)\n'
                                             '            except '
                                             'ModuleNotFoundError:\n'
                                             '                return '
                                             'tools.die(err.is_no_plugin, '
                                             'argument=a)\n'
                                             '            run = getattr(p, '
                                             "'run', None)\n"
                                             '            if run == None:\n'
                                             '                return '
                                             'tools.die(err.is_no_valid_action, '
                                             'action=a)\n'
                                             '            # func args not in '
                                             'config? Potentially typos:\n'
                                             '            # we raise on those, '
                                             'if the sig has no kw args, else '
                                             'we pass them into run:\n'
                                             '            fa = not_conf_args\n'
                                             '            if fa:\n'
                                             '                for k, v in '
                                             'fa.items():\n'
                                             '                    fa[k] = '
                                             'simple_cast(v)\n'
                                             '            s = getargspec(run)\n'
                                             '            kw = {}\n'
                                             '            for a in s.args:\n'
                                             '                v = fa.pop(a, '
                                             'C.get(a))\n'
                                             '                if v is not '
                                             'None:\n'
                                             '                    kw[a] = v\n'
                                             '            if s.keywords:\n'
                                             '                kw.update(fa)\n'
                                             '            else:\n'
                                             '                if fa:\n'
                                             '                    '
                                             'tools.die(err.unknown_parameters, '
                                             "unknown=', '.join([k for k in "
                                             'fa]))\n'
                                             '            ActionResults[a] = '
                                             'run(**kw)\n'
                                             '    ```\n'
                                             '\n'
                                             '=== '
                                             '"[:fontawesome-brands-git-alt:](https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L176)"\n'
                                             '    '
                                             'https://github.com/AXGKl/terminal_markdown_viewer/blob/master/src/mdv/plugins/mdv_conf.py#L176\n'},
 '9b5353521558e132db4a37ebc39b2af5': {'cmd': '$ cat '
                                             '/tmp/mdv_demo/plugs/config.py',
                                      'res': '# '
                                             '------------------------------------------- '
                                             'mdv configuration\n'
                                             "cfg = {'theme': 'blue'}\n"
                                             '\n'
                                             'class Plugins:\n'
                                             '    # mapping this config file '
                                             'itself also as the configurator '
                                             '(i.e. the conf plugin)\n'
                                             "    conf = 'config' \n"
                                             '\n'
                                             '# '
                                             '------------------------------------------ '
                                             'mdv configurator\n'
                                             '# being also conf, we need a '
                                             'configure and run method:\n'
                                             'from mdv.globals import C\n'
                                             'from mdv.plugs import plugins\n'
                                             '\n'
                                             'def configure(argv):\n'
                                             '    C.update(cfg)\n'
                                             '\n'
                                             'def run():\n'
                                             '    # we have the global config\n'
                                             '    print(C)\n'
                                             '    # and can use plugins:\n'
                                             '    print(plugins.view)\n'
                                             '\n'
                                             '    # here you would parse '
                                             'sys.argv and call action '
                                             'plugins...\n'},
 'ef060de93401918768f699b078965ec3': [{'cmd': 'mdv2 --config-dir=/tmp/mdv_demo',
                                       'res': '$ mdv2 '
                                              '--config-dir=/tmp/mdv_demo\n'
                                              "{'theme': 'blue'}\n"
                                              "<module 'mdv.plugins.view' from "
                                              "'/home/gk/repos/terminal_markdown_viewer/src/mdv/plugins/view.py'>"}]}