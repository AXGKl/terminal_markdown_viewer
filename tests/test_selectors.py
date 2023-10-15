from mdv.cli import main

dind = lambda s: s.replace('\n    ', '\n')

# no user plugs:


def cli(args):
    return ''


def test_doc1():
    d = '''
    <style>
    * {background-color: #1b202a}
    body {padding: 2em}
    p {color: rgb(100, 100, 0);}
    h2, #myid {font-style:italic}
    </style>

    # MD Demo Document

    md text => `p` tag

    <h2 id="h2" style='color: blue; padding:1em'>HTML H2 Heading</h2>
    <p id="myid">html p tag</p>

    '''
    pass
