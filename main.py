from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.init_mongo import init_db
from routers.athlete_router import router as athlete_router
from routers.simulation_router import router as simulation_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(athlete_router)
app.include_router(simulation_router)

@app.get("/")
def home():
    return {"Message": "Table Tennis Simulator + FastAPI + MongoDB + Docker"}