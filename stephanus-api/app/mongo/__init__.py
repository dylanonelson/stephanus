from pymongo import MongoClient

from app.parser import parse_rep_xml

client = MongoClient()

db = client.stephanus

pages = db.pages

pages.remove({})

for page in parse_rep_xml.parse_book_one():
    pages.insert_one(page)
