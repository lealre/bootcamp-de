from db import SessionLocal, engine, Base
from models import Pokemon

with SessionLocal() as session:
    pokemon = session.query(Pokemon).filter_by(id = 2).first()
    print(pokemon.name)

