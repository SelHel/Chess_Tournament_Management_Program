from datetime import datetime
from typing import List
from pydantic import BaseModel, validator
from pydantic.types import constr
from .match import Match


class Round(BaseModel):
    """Modèle représentant un round du tournoi d'échec."""
    name: constr(min_length=2, max_length=10)
    start_time: datetime = datetime.now()
    end_time: datetime = None
    matches: List[Match] = []

    @validator("matches")
    def check_matches(cls, value: List[Match]):
        return [Match(**match_data) for match_data in value]
