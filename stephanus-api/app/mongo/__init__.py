from pymongo import MongoClient

from app.parser import parse_rep_xml
from app import app

mongo_url = app.config['MONGO_URL']
mongo_db = app.config['MONGO_DB_NAME']

client = MongoClient(mongo_url)

db = client[mongo_db]

pages = db.pages

pages.remove({})

for page in parse_rep_xml.parse_book_one():
    pages.insert_one(page)
