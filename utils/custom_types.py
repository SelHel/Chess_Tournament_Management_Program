import re
from enum import Enum
from typing import Any

"""Création de nouveaux types personnalisés."""


class Name(str):
    """Classe représentant un nom."""
    def __new__(cls, value: str):
        """
        La méthode __new__ est appelée avant la création d'un objet Name,
        elle vérifie si la valeur passée en paramètre correspond à un nom.

        Paramètres
        ----------
        cls : la classe Name

        value : str
            une chaîne de caractère représentant un nom
        Retour
        ------
        Retourne l'objet nouvellement créé ou lève une ValueError.
        """
        if not re.match("^[a-zA-Z- 'éèïû]{2,25}$", value) and value != "0":
            raise ValueError("Le nom n'est pas valide.")
        return super().__new__(cls, value)


class Gender(Enum):
    """Classe créant une énumération de constantes qui représentent le genre d'un joueur du tournoi."""
    MALE = "M"
    FEMALE = "F"


class PositiveInt(int):
    """Classe représentant un entier positif."""
    def __new__(cls, value: Any):
        """
        La méthode __new__ est appelée avant la création d'un objet PositiveInt,
        elle vérifie si la valeur passée en paramètre correspond à un entier positif.

        Paramètres
        ----------
        value : int
            un entier positif
        Retour
        ------
        Retourne l'objet nouvellement créé ou lève une ValueError.
        """
        if int(value) < 0:
            raise ValueError("Le nombre doit être un entier positif.")
        return super().__new__(cls, value)


class TimeControl(Enum):
    """Classe créant une énumération de constantes qui représentent le type de contrôle du temps d'un tournoi."""
    BULLET = "bullet"
    BLITZ = "blitz"
    FASTMOVE = "coup rapide"


class Score(Enum):
    """Classe créant une énumération de constantes qui représentent le score d'un joueur du tournoi."""
    WIN = 1.0
    LOSE = 0.0
    DRAW = 0.5
    UNKNOWN = -1
