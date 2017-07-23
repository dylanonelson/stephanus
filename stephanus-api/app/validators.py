from app import app
import re

def has_stephanus_shape(s):
    r = r'^\d{1,3}[a-e]$'
    return re.match(r, s) != None

def validate_min_page(f):
    print(app.config['MINIMUM_STEPHANUS_PAGE'])
    return (f >= app.config['MINIMUM_STEPHANUS_PAGE'] and has_stephanus_shape(f))

def validate_max_page(t):
    return (t <= app.config['MAXIMUM_STEPHANUS_PAGE'] and has_stephanus_shape(t))
