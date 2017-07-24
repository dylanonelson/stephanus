#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS
from webargs import fields
from webargs.core import ValidationError
from webargs.flaskparser import use_args
import os

app = Flask(__name__)

CORS(app)

app_env = os.environ.get('PYTHON_ENV')
app_env = app_env if app_env != None else 'development'
app.config.from_object(f"app.config.{app_env}")

from .validators import *
from app.mongo import db

@app.route('/')
def index():
    return (f"Query for pages between {app.config['MINIMUM_STEPHANUS_PAGE']} "
            f"and {app.config['MAXIMUM_STEPHANUS_PAGE']} at /:page or /?from="
            "[page]&to=[page]")

range_args = {'from': fields.Str(required=True, validate=validate_min_page),
              'to': fields.Str(required=True, validate=validate_max_page)}
@app.route('/pages')
@use_args(range_args)
def pages(args):
    from_page = args.get('from')
    to_page = args.get('to')
    query = {'$where': f"(this.id >= '{from_page}' && this.id <= '{to_page}')"}
    matches = db.pages.find(query, { '_id': 0 })
    list = []
    for match in matches:
        list.append(match)
    resp = jsonify(list)
    return resp

@app.route('/<page>')
def page(page):
    if has_stephanus_shape(page) == False:
        raise ValidationError('Invalid format for Stephanus page')

    match = db.pages.find_one({'id': page}, {'_id': 0})
    resp = jsonify(match)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run(app.config['HOST'], port=app.config['PORT'])
