#!flask/bin/python
from flask import Flask, jsonify
import os

app = Flask(__name__)

app_env = os.environ.get('PYTHON_ENV')
app_env = app_env if app_env != None else 'development'
app.config.from_object(f"app.config.{app_env}")

from app.mongo import db

@app.route('/')
def index():
    return "Hello, world!"

@app.route('/<page>')
def page(page):
    match = db.pages.find_one({'id': page}, {'_id': 0})
    resp = jsonify(match)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run(debug=True)
