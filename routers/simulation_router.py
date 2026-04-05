from fastapi import APIRouter
from schemas.athlete_schema import Athlete
from services.athlete_service import get_athlete_by_id_service
from core.match_engine import *

router = APIRouter(prefix="/simulate", tags=["Simulation"])

@router.post("/{j1_id}/{j2_id}")
def simulate_match(j1_id: str, j2_id: str):
    j1 = get_athlete_by_id_service(j1_id)
    j2 = get_athlete_by_id_service(j2_id)
    
    result = match_simulation(j1, j2)
    
    return result
