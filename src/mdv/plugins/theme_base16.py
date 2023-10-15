from mdv.tools import C

i = C
rules = [
    ('body', {'background-color': C['BG']}),
    ('a', {'text-decoration': 'underline', 'color': 'green'}),
    ('ul', {'background-color': 'brown'}),
    ('em', {'font-style': 'italic'}),
    ('strong', {'font-weight': 'bold'}),
    ('code', {'font-style': 'italic', 'background-color': 'grey'}),
    (
        'h1',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H1') or 'lime',
        },
    ),
    (
        'h2',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H2') or 'maroon',
        },
    ),
    (
        'h3',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H3') or 'purple',
        },
    ),
    (
        'h4',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H4') or 'teal',
        },
    ),
    (
        'h5',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H5') or 'yellow',
        },
    ),
    (
        'h6',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H6') or 'red',
        },
    ),
    (
        'h7',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H7') or 'green',
        },
    ),
    (
        'h8',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H8') or 'silver',
        },
    ),
    (
        'h9',
        {
            'font-weight': 'bold',
            'background-color': 'white',
            'color': C.get('H9') or 'navy',
        },
    ),
]
