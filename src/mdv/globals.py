"""
Global data structures
"""


import os

here = os.path.realpath(__file__).rsplit(os.path.sep, 1)[0]
envget = os.environ.get

UserPlugs = set()
# the global config dict, filled by conf plugin:
C = {}
# allows chaining of actions:
ActionResults = {}
UserConfigDir = ['']


class CLI:
    kv = {}
    actions = []
    plugin_run_args = {}


Actions = CLI.actions


# class Finished(Exception):
#     """Action Pipeline Finished"""


class err:
    is_no_plugin = 'Is no plugin'
    is_no_valid_action = 'Is no valid action (no run method)'
    unknown_parameters = 'Unknown parameters'
