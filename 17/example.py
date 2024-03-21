from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session

# conect to a SQLite database in memory
engine = create_engine('sqlite:///17/database.db', echo =True)

print('SQLite connection established!')

Base = declarative_base()

# create table schema
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True)
    name = Column(String, nullable= False)
    age = Column(Integer, nullable= False)

# create database
Base.metadata.create_all(engine)

# insert value with context manager
with Session() as session:
    new_user = User(name='Ana', age=25)
    session.add(new_user)
    # Commit is automatically done here if there are no exceptions
    # Rollback is automatically called if an exception occurs
    # The session is automatically closed when leaving the with block

### this ways works too
# Session = sessionmaker(bind=engine)
# session = Session()

# try:
#     new_user = User(nome='Ana', idade=25)
#     session.add(new_user)
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()