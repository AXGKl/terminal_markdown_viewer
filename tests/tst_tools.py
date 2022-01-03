import os
import sys
from shutil import copyfile
from subprocess import run as srun

# if set, that would hard import plugins in mdv/plugs.py (our IDE trick):
os.environ['MDV_DEV'] = ''

here = os.path.abspath(os.path.dirname(__file__))


def test_mod_ctx(test_file):
    tf = test_file.rsplit('/', 1)[-1].split('.py', 1)[0]
    m = {'d_tmp': os.path.dirname(here) + '/tmp', 'fn_tst': tf}
    m['pth_tst'] = test_file
    m['d_tmp_tst'] = '%(d_tmp)s/tests/%(fn_tst)s' % m
    m['d_plugs_tst'] = '%(d_tmp_tst)s/plugs' % m
    return m


def clear_dir(d):
    """keep d intact"""
    assert len(d.split('/')) > 3
    for root, dirs, files in os.walk(d):
        for file in files:
            os.remove(os.path.join(root, file))


def run_proc(cmd):

    cmd = cmd if isinstance(cmd, list) else cmd.split(' ')
    # add --debug at the end to debug with breakpoints in the inner process:
    # we do not need pytest's --debug option
    if sys.argv[-1] == '--debug':
        sys.argv.pop()
        cmd = ' '.join(cmd)
        print('\n--debug is set - running in foreground for debugging')
        breakpoint()  # FIXME BREAKPOINT
        res = os.system(cmd)
        sys.exit(res)

    p = srun(cmd, capture_output=True)
    return p.returncode, p.stdout.decode(), p.stderr.decode()


in_mdv = lambda: sys.argv[0].endswith('mdv2')


def prepare_custom_user_conf_dir(pth_tst, fn_tst, d_tmp_tst, d_plugs_tst, **kw):
    """Prepares a user config directory with the test module and the tools in it"""
    assert not in_mdv()
    # os.environ['CONFIG_DIR'] = d_tmp_tst
    os.makedirs(d_plugs_tst, exist_ok=True)
    clear_dir(d_tmp_tst)
    copyfile(pth_tst, f'{d_plugs_tst}/{fn_tst}.py')
    copyfile(__file__, f'{d_plugs_tst}/tst_tools.py')


def current_test_func():
    ct = os.environ.get('PYTEST_CURRENT_TEST')
    return ct.split('::', 1)[1].split(' ', 1)[0] if ct else ''
