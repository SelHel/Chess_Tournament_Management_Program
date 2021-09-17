from datetime import date
from pydantic import BaseModel, PositiveInt, validator
from utils.custom_types import Name, Gender
from utils.manager import Manager


class Player(BaseModel):
    """Model representing a chess player."""
    id: PositiveInt
    last_name: Name
    first_name: Name
    birth_date: date
    gender: Gender
    rank: PositiveInt


    @validator("birth_date")
    def check_player_age(cls, value):
        today = date.today()
        player_age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if player_age < 16:
            raise ValueError("Le joueur doit avoir au minimum 16 ans.")
        return value


player_manager = Manager(Player, lambda x: x.id)
