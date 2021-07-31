from typing import List
from datetime import datetime
from collections import Counter

from pydantic import BaseModel, PositiveInt, validator

from .round import Round
from .player import player_manager as pm
from utils.manager import Manager


class Tournament(BaseModel):
    """Model representing a chess tournament."""

    id: PositiveInt
    name: str
    location: str
    start_date: str
    end_date: str
    number_rounds: PositiveInt
    rounds: List[dict]
    players: list
    time_control: str
    description: str

    @validator("location", "name")
    def check_len_name(cls, value):
        if len(value) > 25:
            raise ValueError("Le nom du tournoi ne doit pas dépasser 25 caractères.")
        return value

    @validator("start_date", "end_date")
    def check_date_format(cls, value):
        try:
            datetime.fromisoformat(value)
        except ValueError:
            raise ValueError("La date du tournoi doit être au format AAAA-MM-JJ HH:mm.")
        return value

    @validator("end_date")
    def check_dates_match(cls, value, values):
        if value < values["start_date"]:
            raise ValueError("La date de fin du tournoi doit être supérieure ou égale à la date de début.")
        return value

    @validator("players")
    def check_players(cls, value):
        count = Counter(value)
        for c in dict(count):
            if count[c] > 1:
                raise ValueError("Un joueur ne peut pas s'inscrire plusieurs fois dans un tournoi.")
        for player_id in value:
            pm.find_by_id(player_id)
        return value

    @validator("time_control")
    def check_time_control(cls, value):
        if value.lower() not in ("bullet", "blitz", "coup rapide"):
            raise ValueError("Le contrôle du temps doit être un bullet, un blitz ou un coup rapide.")
        return value.lower()

    @validator("description")
    def check_description(cls, value):
        if len(value) > 150:
            raise ValueError("La description du tournoi ne doit pas dépasser 150 caractères.")
        return value

    @validator("rounds")
    def check_rounds(cls, value: List[dict]):
        value = [Round(**round_data) for round_data in value]
        return value


tournament_manager = Manager(Tournament, lambda x: x.id)
