from fastapi import APIRouter
from schemas.athlete_schema import Athlete
from services.athlete_service import *

router = APIRouter(prefix="/athletes", tags=["Athletes"])

#GET - get all athletes
@router.get("/")
def list_all_athletes():
    return get_all_athletes_service()

#POST - create athlete
@router.post("/")
def create_athlete(athlete: Athlete):
    return create_athlete_service(athlete)

#GET - get athlete by id
@router.get("/id/{athlete_id}")
def get_athlete_id(athlete_id: str):
    return get_athlete_by_id_service(athlete_id)

#GET - get athlete by name
@router.get("/name/{athlete_name}")
def get_athlete_name(athlete_name: str):
    return get_athlete_by_name_service(athlete_name)

#PUT - update athlete
@router.put("/update/{athlete_id}")
def update_athlete(athlete_id: str, athlete: Athlete):
    return update_athlete_service(athlete_id, athlete)

#DELETE - delete athlete
@router.delete("/delete/{athlete_id}")
def delete_athlete(athlete_id: str):
    return delete_athlete_service(athlete_id)
