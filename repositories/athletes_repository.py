from database.mongo import athletes_collection
from bson import ObjectId

def create_athlete(athlete_dict):
    return athletes_collection.insert_one(athlete_dict)

def get_all_athletes():
    return athletes_collection.find()

def get_athlete_by_id(athlete_id):
    return athletes_collection.find_one({"_id": ObjectId(athlete_id)})

def get_athlete_by_name(athlete_name):
    return athletes_collection.find_one({"name": athlete_name})

def update_athlete(athlete_id, athlete_dict):
    return athletes_collection.update_one(
        {"_id": ObjectId(athlete_id)},
        {"$set": athlete_dict}
    )

def delete_athlete(athlete_id):
    return athletes_collection.delete_one({"_id": ObjectId(athlete_id)})
