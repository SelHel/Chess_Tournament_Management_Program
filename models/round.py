from datetime import datetime
from typing import List
from pydantic import BaseModel
from pydantic.types import constr
from .match import Match


class Round(BaseModel):
    """
    Modèle représentant un round du tournoi d'échec.

    Champs obligatoires
    -------------------
    name : constr(min_length=2, max_length=10)
        Utilisation de la fonction de type constr pour définir une longueur minimale et maximale du nom du round
    start_time : datetime
        La date et heure de début du round
    end_time : datetime
        La date et heure de fin du round
    matches : List[Match]
        La liste des matchs du round
    """
    name: constr(min_length=2, max_length=10)
    start_time: datetime = datetime.now()
    end_time: datetime = None
    matches: List[Match] = []
