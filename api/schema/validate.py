from jsonschema import validate
from termcolor import cprint
import json

with open('./stephanus_page.json') as file:
    schema = json.load(file)

with open('./examples/327a.json') as file:
    example = json.load(file)

try:
    validate(example, schema)
    cprint ('VALID!', 'green')
except Exception as e:
    cprint(e, 'red')
