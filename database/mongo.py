from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient(MONGO_URL)

db = client["table_tennis_sim"]

athletes_collection = db["athletes"]
