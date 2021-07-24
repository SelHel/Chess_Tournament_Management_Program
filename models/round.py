from typing import List

from pydantic import BaseModel, validator

from .match import Match


class Round(BaseModel):
    """Model representing a round of the chess tournament."""
    name: str
    start_time: str
    end_time: str
    matches: List[dict]

    @validator("name")
    def check_len_name(cls, value: str):
        if len(value) > 25:
            raise ValueError("Le nom du round ne doit pas dépasser 25 caractères.")
        return value
    
    @validator("matches")
    def check_matches(cls, value: List[dict]):
        value = [Match(**match_data) for match_data in value]
        return value