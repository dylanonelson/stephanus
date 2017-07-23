#!flask/bin/python
from flask import Flask, jsonify, request
from webargs import fields
from webargs.core import Parser
from webargs.flaskparser import use_args
import os

app = Flask(__name__)

app_env = os.environ.get('PYTHON_ENV')
app_env = app_env if app_env != None else 'development'
app.config.from_object(f"app.config.{app_env}")

from .validators import *
from app.mongo import db

index_args = {'from': fields.Str(required=True, validate=validate_min_page),
              'to': fields.Str(required=True, validate=validate_max_page)}

@app.route('/')
@use_args(index_args)
def index(args):
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
    match = db.pages.find_one({'id': page}, {'_id': 0})
    resp = jsonify(match)
    resp.status_code = 200
    return resp
