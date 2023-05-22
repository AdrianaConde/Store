import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password='postgres',
    port= 5432,
    host="localhost",
    database="store"
)

def get_engine():
    print(os.getenv('DATABASE'))
    engine = create_engine(url=os.getenv('DATABASE'), echo=True, echo_pool=True)
    return engine

def get_session():
    engine = get_engine()
    session = Session(engine)
    return session
