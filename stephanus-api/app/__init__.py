#!flask/bin/python
from flask import Flask
from app.mongo import db

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
