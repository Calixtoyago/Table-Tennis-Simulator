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
@router.get("//{athlete_id}")
def get_athlete(athlete_id: str):
    return get_athlete_by_id_service(athlete_id)

#PUT - update athlete
@router.put("//{athlete_id}")
def update_athlete(athlete_id: str, athlete: Athlete):
    return update_athlete_service(athlete_id, athlete)

#DELETE - delete athlete
@router.delete("//{athlete_id}")
def delete_athlete(athlete_id: str):
    return delete_athlete_service(athlete_id)
