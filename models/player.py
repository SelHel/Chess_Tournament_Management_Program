import re
from datetime import date

from pydantic import BaseModel, validator

from utils import Manager

class Player(BaseModel):
    """Model representing a chess player."""
    id: int
    last_name: str
    first_name: str
    birth_date: str
    gender: str
    rank: int

    @validator("id")
    def _check_id(cls, value):
        if value < 0:
            raise ValueError("L'identifiant doit être un nombre entier positif.")
        return value

    @validator("last_name", "first_name")
    def _check_names(cls, value):
        if not re.match("^[a-zA-Z- 'éèïû]{2,25}$", value):
            raise ValueError("Le nom du joueur n'est pas valide.")
        return value
        
    @validator("birth_date")
    def _check_date_format(cls, value: str):
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError("La date doit être au format AAAA-MM-JJ.")
        return value
        
    @validator("birth_date")
    def _check_player_age(cls, value):
        today = date.today()
        bd = date.fromisoformat(value)
        player_age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
        if player_age < 16:
            raise ValueError("Le joueur doit avoir au minimum 16 ans.")
        return value

    @validator("gender")
    def _check_gender(cls, value):
        if value.capitalize() not in ("Homme", "Femme"):
            raise ValueError("Le genre doit être Homme ou Femme.")
        return value.capitalize()

    @validator("rank")
    def _check_rank(cls, value):
        if value <= 0:
            raise ValueError("Le classement doit être un nombre entier positif.")
        return value

    def __str__(self):
        return f"Joueur {self.id}: {self.first_name} {self.last_name}, {self.birth_date}, {self.gender}, classement : {self.rank}"
    
player_manager = Manager(Player, lambda x: x.id)