rules = [
    ('em', {'font-style': 'italic'}),
    ('strong', {'font-weight': 'bold'}),
    ('code', {'font-style': 'italic', 'background-color': 'grey'}),
]

hcs = ['lime', 'maroon', 'purple', 'teal', 'yellow', 'red', 'green', 'silver', 'navy']
for level, hc in zip(range(1, len(hcs) + 1), hcs):
    rules.insert(level - 1, (f'h{level}', {'font-weight': 'bold', 'color': hc}))
