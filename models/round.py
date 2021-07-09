from datetime import datetime
from typing import List

from pydantic import BaseModel, validator

from .match import Match

class Round(BaseModel):
    """Model representing a round of the chess tournament."""
    name: str
    start_time: datetime = datetime.now().isoformat()
    end_time: datetime
    matches : List[dict]

    @validator("name")
    def _check_len_name(cls, value: str):
        if isinstance(value, str):
            if len(value) > 25:
                raise ValueError("Le nom ne doit pas dépasser 25 caractères.")
        else:
            raise ValueError("Le nom doit être une chaîne de caractères.")
        return value
    
    @validator("matches")
    def _check_matches(cls, value: List[dict]):
        value = [Match(**match_data) for match_data in value]
        return value


