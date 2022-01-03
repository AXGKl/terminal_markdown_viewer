"""
End to End Testing the plugin and configuration machinery

This module is pretending to be an action plugin for mdv, with a run method, which knows
the calling test function
"""
import os
import sys

# when within mdv we need the second form:
try:
    import tst_tools as t
except:
    from . import tst_tools as t

import mdv
from mdv.globals import err as Err
from mdv.tools import write_file
from mdv.globals import C

# holds directories
ctx = t.test_mod_ctx(__file__)

mdv2 = lambda: 'mdv2 --config-dir=%(d_tmp_tst)s ' % ctx


def run(**kw):
    """we are in a subprocess, called by mdv as action plugin's run func"""
    globals()[t.current_test_func()](in_mdv=True, **kw)


def test_is_no_plugin():
    cmd = mdv2() + '--k1=v1 --k2 v2 noactiontest --k3=v3 xxx --k4 v4'
    st, out, err = t.run_proc(cmd)
    assert st > 0 and not out and Err.is_no_plugin in err and 'noactiontest' in err
    # did not even try xxx:
    assert not 'xxx' in err


def test_exception_raised(in_mdv=False, **kw):
    if in_mdv:
        # test args casting:
        i = 9 / 0

    # when one is known the other not:
    t.prepare_custom_user_conf_dir(**ctx)
    cmd = mdv2() + '--kv1=1 %(fn_tst)s --kv2=bar' % ctx
    st, out, err = t.run_proc(cmd)
    assert st and 'ZeroDivision' in err


def test_is_no_plugin_one_known_other_not(in_mdv=False, **kw):
    if in_mdv:
        # test args casting:
        assert C['kv1'] == 1.0 and C['kv2'] == 'bar'
        return print('within')

    # when one is known the other not:
    t.prepare_custom_user_conf_dir(**ctx)
    cmd = mdv2() + '--kv1=1 %(fn_tst)s foo --kv2=bar' % ctx
    st, out, err = t.run_proc(cmd)
    # had run fn_tst action plugin, which was printing this on stdout:
    assert 'within' in out
    # but then failed, trying foo:
    assert st > 0 and Err.is_no_plugin in err and 'foo' in err


def test_is_no_action_plugin():
    t.prepare_custom_user_conf_dir(**ctx)
    write_file('mytmod.py', '# test', dir=ctx['d_plugs_tst'])
    st, out, err = t.run_proc(mdv2() + '--foo=bar mytmod xxx')
    assert st > 0 and not out and Err.is_no_valid_action in err and 'mytmod' in err


# for the next test we need a run method w/o **kw args:
run = (lambda k1: None) if 'test_unknown_cli_args' in t.current_test_func() else run


def test_unknown_cli_args(in_mdv=False):
    """If the user specifies params which are neither configured nor in the run sig
    he gets them listed on stderr

    Note: We rewrote the run method for this specific test, see 3 lines above
    """
    t.prepare_custom_user_conf_dir(**ctx)
    # k1 known, the others not, configured: None:
    cmd = mdv2() + '--k1=v1 --k2 v2 %(fn_tst)s --k3=v3 --k4 v4' % ctx
    st, out, err = t.run_proc(cmd)
    assert st > 0 and not out and Err.unknown_parameters in err
    # k1 is in the run signature, i.e. not in err
    assert 'k1' not in err
    for k in range(2, 5):
        assert 'k%s' % k in err
