import os

here = os.path.dirname(__file__)
root = here.split('/tests', 1)[0]


def test_make():
    d = os.getcwd()
    os.chdir(root)
    h = os.popen('source ./make; make -h').read()
    assert 'tests' in h and 'Usage' in h and 'Aliases' in h and 'docs' in h
    os.chdir(d)
