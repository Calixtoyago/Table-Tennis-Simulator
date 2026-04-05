from repositories.athletes_repository import *
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from schemas.athlete_schema import Athlete

def format_athlete(athlete):
    athlete["_id"] = str(athlete["_id"])
    return athlete

def get_all_athletes_service():
    athletes = get_all_athlete()
    return [format_athlete(athlete) for athlete in athletes]

def create_athlete_service(athlete):
    try:
        result = create_athlete(athlete.model_dump())
    except DuplicateKeyError as dke:
        return {"error": dke}
    return {"message": "Athlete Created", "id": str(result.inserted_id)}

def get_athlete_by_id_service(user_id):
    try:
        athlete = get_athlete_by_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not Found")
    athlete["_id"] = str(athlete["_id"])
    return Athlete(**athlete)

def update_athlete_service(athlete_id, athlete):
    try:
        result = update_athlete(athlete_id, athlete.model_dump())
    except DuplicateKeyError:
        return {"error": "Name already used"}
    except Exception as e:
        return {"error": e}
    if result.matched_count == 0:
        return {"error": "Athlete not found"}
    return {"message": "Athlete Updated"}

def delete_athlete_service(athlete_id):
    try:
        result = delete_athlete(athlete_id)
    except Exception as e:
        return {"error": e}
    if result.deleted_count == 0:
        return {"error": "Athlete not found"}
    return {"message": "Athlete deleted"}
