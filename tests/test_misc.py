import os

here = os.path.dirname(__file__)
root = here.split('/tests', 1)[0]


def test_make():
    h = os.popen(root + '/make -h').read()
    assert 'tests' in h and 'Usage' in h and 'Aliases' in h and 'docs_regen' in h
