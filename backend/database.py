# Required imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# What we are calling the database
SQLALCHAMY_DATABASE_URL='sqlite:///./persona.db'

# Code to run command in main.py
engine=create_engine(SQLALCHAMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
# Code for models.py to run
Base=declarative_base()

# Code to get info and then close when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()