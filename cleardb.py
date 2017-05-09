import pymongo
from pymongo import MongoClient

client = MongoClient('localhost')
db = client.test_database
collection = db.test_collection


collection.remove({})
