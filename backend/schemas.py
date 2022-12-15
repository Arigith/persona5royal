# Required imports
from pydantic import BaseModel

# What information to show from the database
class PersonaBase(BaseModel):
    arcana: str
    persona_name: str
    starting_level: int
    class Config():
        orm_mode=True