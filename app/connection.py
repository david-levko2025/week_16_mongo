import json
from pymongo import MongoClient
from os import getenv

mongo_uri = getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")
file_path = './employee.json'

def get_connection():
    myclient = MongoClient(mongo_uri)
    db = myclient["contacts_data"]
    Collection = db["employee"]
    return Collection
collection = get_connection()


# mongo_uri = getenv("MONGO_URI", "mongodb+srv://mdavidl2003:mdavidl2003@cluster0.1n6f8x2.mongodb.net/")

# Loading or Opening the json file
# with open(file_path) as file:
#     file_data = json.load(file)

# # Inserting the loaded data in the Collection
# ins_result = get_connection.insert_many(file_data)
# print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")