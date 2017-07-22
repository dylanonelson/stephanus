#!flask/bin/python
from flask import Flask, jsonify
from app.mongo import db

app = Flask(__name__)

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
