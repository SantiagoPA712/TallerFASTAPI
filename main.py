from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine, get_db
import models
from models import PlayerDB

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "FastAPI está funcionando correctamente"}

# Modelo Pydantic para validar la creación de un nuevo jugador
class PlayerCreate(BaseModel):
    name: str
    height: int

@app.get("/players/")
def get_players(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    players = db.query(PlayerDB).offset(skip).limit(limit).all()
    return players

@app.post("/players/")
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    # Crear un nuevo jugador en la base de datos
    new_player = PlayerDB(name=player.name, height=player.height)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return {"message": "Jugador creado exitosamente", "player": new_player}
