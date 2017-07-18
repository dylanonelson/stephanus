import json
import os

dir = os.path.dirname(__file__)
fn = os.path.join(dir, 'stephanus_page.json')

with open(fn) as f:
    schema = json.load(f)