import re
from enum import Enum


class Name(str):
    def __init__(self, value: str):
        if not re.match("^[a-zA-Z- 'éèïû]{2,25}$", value):
            raise ValueError("Le nom n'est pas valide.")
        super().__init__()


class Gender(str, Enum):
    Male = "M"
    Female = "F"
