from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text


engine = create_engine("sqlite:///16/database.db")

with Session(engine) as session:

    statement = text("SELECT * FROM hero;")    

    results = session.exec(statement)
    
    heroes = results.fetchall()
    
    for hero in heroes:
        print(hero)