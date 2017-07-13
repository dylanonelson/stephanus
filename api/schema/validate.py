from jsonschema import validate
from termcolor import cprint
import json

examples = []

with open('./stephanus_page.json') as f:
    schema = json.load(f)

with open('./examples/327a.json') as f:
    p327a = json.load(f)
    examples.append(p327a)

with open('./examples/327c.json') as f:
    p327c = json.load(f)
    examples.append(p327c)

try:
    for ex in examples:
        validate(ex, schema)
    cprint ('VALID!', 'green')
except Exception as e:
    cprint(e, 'red')
