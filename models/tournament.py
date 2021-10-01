from typing import List
from datetime import datetime
from collections import Counter
from pydantic import BaseModel, PositiveInt, validator
from .round import Round
from .player import player_manager as pm
from utils.manager import Manager
from utils.custom_types import TimeControl


class Tournament(BaseModel):
    """ Modèle représentant un tournoi d'échec """
    id: PositiveInt
    name: str
    location: str
    start_date: datetime
    end_date: datetime = None
    number_rounds: PositiveInt
    rounds: List[dict] = []
    players: list
    time_control: TimeControl
    description: str

    @validator("location", "name")
    def check_len_name(cls, value):
        if len(value) > 25:
            raise ValueError("Le nom du tournoi ne doit pas dépasser 25 caractères.")
        return value

    @validator("end_date")
    def check_dates_match(cls, value, values):
        if value < values["start_date"]:
            raise ValueError("La date de fin du tournoi doit être supérieure ou égale à la date de début.")
        return value

    @validator("players")
    def check_nb_players(cls, value):
        if len(value) < 2 or len(value) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair et supérieur ou égal à 2.")
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
