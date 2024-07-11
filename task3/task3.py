import json


def val_func(d1, d2):
    try:
        d2['value'] = d1[d2['id']]
    except KeyError:
        pass
    try:
        for value in d2['values']:
            val_func(d1, value)
    except KeyError:
        pass


with open('values.json') as file:
    v = json.load(file)
    values = {}
    for value in v['values']:
        values[value['id']] = value['value']

with open('tests.json') as file:
    tests = json.load(file)

    for t in tests['tests']:
        val_func(values, t)

with open('report.json', 'w') as file:
    json.dump(tests, file)