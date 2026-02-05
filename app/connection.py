import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongodb://mongodb-gerstnir-dev.apps.rm2.thpm.p1.openshiftapps.com:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = './employee_data_advanced.json'

def get_connection():
    myclient = MongoClient(mongo_uri)
    db = myclient["fastapi"]

    # Created or Switched to collection
    # names: GeeksForGeeks
    Collection = db[mongo_collection]
    return Collection

# Loading or Opening the json file
with open(file_path) as file:
    file_data = json.load(file)

# Inserting the loaded data in the Collection
ins_result = get_connection.insert_many(file_data)
print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")