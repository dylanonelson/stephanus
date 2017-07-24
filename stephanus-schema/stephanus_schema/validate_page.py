from jsonschema import validate

from stephanus_schema.definitions import schema

def validate_page(json):
    validate(json, schema)
