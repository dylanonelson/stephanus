import jsonref
import os

dir = os.path.dirname(__file__)
fn = os.path.join(dir, 'stephanus_page.json')

with open(fn) as f:
    schema = jsonref.load(f, base_uri=f"file://{fn}")
