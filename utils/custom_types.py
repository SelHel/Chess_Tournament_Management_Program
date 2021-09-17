import re
from enum import Enum
from typing import Any


class Name(str):
    def __new__(cls, value: str):
        if not re.match("^[a-zA-Z- 'éèïû]{2,25}$", value):
            raise ValueError("Le nom n'est pas valide.")
        return super().__new__(cls, value)


class Gender(str, Enum):
    Male = "M"
    Female = "F"


class PositiveInt(int):
    def __new__(cls, value: Any):
        if int(value) < 0:
            raise ValueError("Le nombre doit être un entier positif.")
        return super().__new__(cls, value)


class TimeControl(str, Enum):
    Bullet = "bullet"
    Blitz = "blitz"
    FastMove = "coup rapide"
