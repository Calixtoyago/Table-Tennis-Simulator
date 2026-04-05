from repositories.athletes_repository import *
from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
from schemas.athlete_schema import Athlete

def format_athlete(athlete):
    athlete["_id"] = str(athlete["_id"])
    return athlete

def get_all_athletes_service():
    athletes = get_all_athletes()
    return [format_athlete(athlete) for athlete in athletes]

def create_athlete_service(athlete):
    try:
        result = create_athlete(athlete.model_dump())
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Athlete already exists")
    return {"message": "Athlete Created", "id": str(result.inserted_id)}

def get_athlete_by_id_service(athlete_id):
    try:
        athlete = get_athlete_by_id(athlete_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not Found")
    athlete = format_athlete(athlete)
    return Athlete(**athlete)

def get_athlete_by_name_service(athlete_name):
    try:
        athlete = get_athlete_by_name(athlete_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not Found")
    athlete = format_athlete(athlete)
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
