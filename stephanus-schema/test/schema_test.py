from .context import validate_page
import json
import os
import pytest

def get_example_file(name):
    dir = os.path.dirname(__file__)
    fn = os.path.join(dir, 'examples/' + name)
    with open(fn) as f:
        return json.load(f)

@pytest.fixture
def valid_basic_paragraph():
    return get_example_file('327a.json')

@pytest.fixture
def valid_long_basic_paragraph():
    return get_example_file('327c.json')

def test_valid_basic_paragraph(valid_basic_paragraph):
    validate_page(valid_basic_paragraph)

def test_valid_long_basic_paragraph(valid_long_basic_paragraph):
    validate_page(valid_long_basic_paragraph)
