from jsonschema import validate

from schema.definitions import schema

def validate_page(json):
    validate(json, schema)
