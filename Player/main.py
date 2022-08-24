import logging
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi.middleware.cors import CORSMiddleware

from repository.PlayerRepository import PlayerRepository
from service.PlayerService import PlayerService
from entity.PlayerEntity import Player

# test db as of now, there are present issues connecting to db from docker container
# engine = create_engine("postgresql://postgres@localhost:5432/testDB")
engine = create_engine("postgresql://lgmcmlinxnxscx:b82b8644e80fb385cc86b178f883927ff6558d4dc9b4097ea7a475639e7875dd@ec2-34-253-119-24.eu-west-1.compute.amazonaws.com:5432/drnj22t938aj3")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# can only be used in fastapi routes.. so not sure if its a wise design to pass through this every layer
def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# set up classes
playerRepository = PlayerRepository(engine)
playerService = PlayerService(playerRepository)

# set log level
logging.basicConfig(level=logging.DEBUG)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/api/players/", response_model=List[Player])
async def get_players():
    players = playerService.get_players()

    if players is None:
        raise HTTPException(status_code=404, detail="No quizzes found")

    return players


@app.get("/api/player/{player_id}", response_model=Player)
async def get_player(player_id: int):
    player = playerService.get_player(player_id)

    if player is None:
        raise HTTPException(
            status_code=404, detail=f"player with id: {player_id} not found")

    return player


@app.post("/api/create/", response_model=Player)
async def create_player(player: Player):
    result = playerService.create_player(player)

    if result == None:
        raise HTTPException(
            status_code=500, detail=f"Unable to create player for id: {player.id}")

    return result


@app.put("/api/update/", response_model=Player)
async def update_player(player: Player):
    result = playerService.update_player(player)

    if result is None:
        raise HTTPException(
            status_code=500, detail=f"Unable to update player with id: {player.id}")

    return result


@app.delete("/api/delete/{player_id}", response_model=Player)
async def delete_player(player_id: int):
    result = playerService.delete_player(player_id)

    if result is None:
        raise HTTPException(
            status_code=500, detail=f"Unable to delete player for id: {player_id}")

    return result
