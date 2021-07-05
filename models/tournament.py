import re
from typing import List
from datetime import datetime

from pydantic import BaseModel, validator

from .player import player_manager as pm
from utils import Manager


class Tournament(BaseModel):
    """Model representing a chess tournament."""

    id: int
    name: str
    location: str
    start_date: str
    end_date: str
    number_rounds: int
    rounds: list
    players: list
    time_control: str
    description: str

    
    @validator("id")
    def _check_id(cls, value):
        if value < 0:
            raise ValueError("L'identifiant doit être un nombre entier positif.")
        return value
    
    @validator("location", "name")
    def _check_len_name(cls, value):
        if len(value) > 25:
            raise ValueError("Le nom ne doit pas dépasser 25 caractères.")
        return value
    
    @validator("start_date", "end_date")
    def _check_date_format(cls, value):
        try:
            datetime.fromisoformat(value)
        except ValueError:
            raise ValueError("La date doit être au format AAAA-MM-JJ HH:mm.")
        return value
    
    @validator("end_date")
    def dates_match(cls, value, values):
        if value < values["start_date"]:
            raise ValueError("La date de fin doit être supérieure ou égale à la date de début.")
        return value
    
    @validator("number_rounds")
    def _check_number_rounds(cls, value):
        if value <= 0:
            raise ValueError("Le nombre de round doit être un nombre entier positif.")
        return value
    
    @validator("players")
    def _check_players(cls, value):
        for player_id in value:
            pm.find_by_id(player_id)
        return value
    
    @validator("time_control")
    def _check_time_control(cls, value):
        if value.lower() not in ("bullet", "blitz", "coup rapide"):
            raise ValueError("Le contrôle du temps est un bullet, un blitz ou un coup rapide")
        return value.lower()
    
    @validator("description")
    def _check_description(cls, value):
        if len(value) > 150:
            raise ValueError("La description ne doit pas dépasser 150 caractères.")
        return value
    

tournament_manager = Manager(Tournament, lambda x: x.id)