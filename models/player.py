from datetime import date

from pydantic import BaseModel, PositiveInt, validator

from utils.custom_types import Name, Gender
from utils.manager import Manager


class Player(BaseModel):
    """Model representing a chess player."""
    id: PositiveInt
    last_name: Name
    first_name: Name
    birth_date: str
    gender: Gender
    rank: PositiveInt


    @validator("birth_date")
    def check_date_format(cls, value: str):
        try:
            date.fromisoformat(value)
        except ValueError:
            raise ValueError("La date de naissance du joueur doit être au format AAAA-MM-JJ.")
        return value
               
    @validator("birth_date")
    def check_player_age(cls, value):
        today = date.today()
        bd = date.fromisoformat(value)
        player_age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
        if player_age < 16:
            raise ValueError("Le joueur doit avoir au minimum 16 ans.")
        return value

    def __str__(self):
        return f"Joueur {self.id}: {self.first_name} {self.last_name}, {self.birth_date}, {self.gender}, classement : {self.rank}"
   

player_manager = Manager(Player, lambda x: x.id)