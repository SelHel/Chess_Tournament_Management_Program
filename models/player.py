from datetime import date
from pydantic import BaseModel, PositiveInt, validator
from utils.custom_types import Name, Gender


class Player(BaseModel):
    """Modèle représentant un joueur d'échec."""
    id: PositiveInt
    last_name: Name
    first_name: Name
    birth_date: date
    gender: Gender
    rank: PositiveInt

    def __str__(self) -> str:
        """Retourne le Nom et Prénom du joueur."""
        return f"{self.last_name} {self.first_name}"

    @validator("birth_date")
    def check_player_age(cls, value):
        """Vérifie si la date de naissance du joueur entrée par l'utilisateur correspond à l'âge minimum requis."""
        today = date.today()
        player_age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if player_age < 16:
            raise ValueError("Le joueur doit avoir au minimum 16 ans.")
        return value
