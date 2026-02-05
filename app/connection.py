import json
from pymongo import MongoClient
from os import getenv

mongo_uri = getenv("MONGO_URI", "fastapi")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = './employee.json'

def get_connection():
    myclient = MongoClient(mongo_uri)
    db = myclient["contacts_data"]
    Collection = db["employee"]
    return Collection
collection = get_connection()
