from datetime import date
from pydantic import BaseModel, validator


class Tournament(BaseModel):
    """Model representing a chess tournament."""
    id: int
    name: str
    location: str
    tournament_date: date
    rounds = None
    rounds_number = None
    players_number = None
    time_control: list
    description: str
    
    @validator('id')
    def _check_id(cls, value):
        if value <= 0:
            raise ValueError("L'identfiant doit être un nombre entier positif.")
        return value
    
    