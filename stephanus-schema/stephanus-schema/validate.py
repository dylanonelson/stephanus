from jsonschema import validate
from termcolor import cprint
import json

with open('./stephanus_page.json') as f:
    schema = json.load(f)

examples = [
    './examples/327a.json',
    './examples/327c.json',
]

try:
    for example in examples:
        with open(example) as f:
            p = json.load(f)
            validate(p, schema)

    cprint ('VALID!', 'green')

except Exception as e:
    cprint(e, 'red')
