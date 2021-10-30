import re
from enum import Enum
from typing import Any


class Name(str):
    def __new__(cls, value: str):
        """Vérifie si le nom entré par l'utilisateur est valide."""
        if not re.match("^[a-zA-Z- 'éèïû]{2,25}$", value) and value != "0":
            raise ValueError("Le nom n'est pas valide.")
        return super().__new__(cls, value)


class Gender(Enum):
    """Classe qui crée une énumération de constantes du genre d'un joueur du tournoi."""
    MALE = "M"
    FEMALE = "F"


class PositiveInt(int):
    def __new__(cls, value: Any):
        """Vérifie si le nombre entré par l'utilisateur est un entier positif."""
        if int(value) < 0:
            raise ValueError("Le nombre doit être un entier positif.")
        return super().__new__(cls, value)


class TimeControl(Enum):
    """Classe qui crée une énumération de constantes du type de contrôle du temps d'un tournoi."""
    BULLET = "bullet"
    BLITZ = "blitz"
    FASTMOVE = "coup rapide"


class Score(Enum):
    """Classe qui crée une énumération de constantes du score d'un joueur du tournoi."""
    WIN = 1.0
    LOSE = 0.0
    DRAW = 0.5
    UNKNOWN = -1
