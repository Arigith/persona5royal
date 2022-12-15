# Required imports
from sqlalchemy import Column, Integer, String
from database import Base

# Table information required in the database
class Persona(Base):
    __tablename__='Personas'
    id=Column(Integer,primary_key=True,index=True)
    arcana=Column(String)
    persona_name=Column(String)
    starting_level=Column(Integer)