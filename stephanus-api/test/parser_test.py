from .context import parser
import stephanus_schema
import pytest

def test_parse_book_one():
    json = parser.parse_rep_xml.parse_book_one()
    for p in json:
        stephanus_schema.validate_page(p)
