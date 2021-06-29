import re
from datetime import date, datetime
from pydantic import BaseModel, validator


class Player(BaseModel):
    """Model representing a chess player."""
    id: int
    last_name: str
    first_name: str
    birth_date: str
    gender: str
    rank: int

    @validator('id')
    def _check_id(cls, value):
        if value <= 0:
            raise ValueError("L'identfiant doit être un nombre entier positif.")
        return value

    @validator('last_name', 'first_name')
    def _check_names(cls, value):
        if not re.match("[a-zA-Z- ']", value):
            raise ValueError("Le nom du joueur n'est pas valide.")
        return value
        
    @validator('birth_date')
    def _check_date_format(cls, value):
        try:
            datetime.strptime(value, "%Y/%m/%d").date()
        except ValueError:
            raise ValueError("La date doit être au format AAAA/MM/JJ.")
        return value
        
    @validator('birth_date')
    def _check_player_age(cls, value):
        today = date.today()
        value = datetime.strptime(value, "%Y/%m/%d").date()
        player_age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if player_age < 16:
            raise ValueError('Le joueur doit avoir au minimum 16 ans.')

    @validator('gender')
    def _check_gender(cls, value):
        if not value == 'Homme' or value == 'Femme':
            raise ValueError('Le genre doit être Homme ou Femme.')
        return value

    @validator('rank')
    def _check_rank(cls, value):
        if value <= 0:
            raise ValueError('Le classement doit être un nombre entier positif.')
        return value

    def __str__(self):
        return f"Joueur {self.id}: {self.first_name} {self.last_name}, {self.birth_date}, {self.gender}, classement : {self.rank}"