from typing import List
from datetime import datetime
from collections import Counter
from pydantic import BaseModel, PositiveInt, validator
from models.match import Match
from .round import Round
from utils.custom_types import TimeControl
from utils.player_manager import pm
from utils.player_id import PlayerId


class Tournament(BaseModel):
    """ Modèle représentant un tournoi d'échec """
    id: PositiveInt
    name: str
    location: str
    start_date: datetime = datetime.today()
    end_date: datetime = None
    number_rounds: PositiveInt
    rounds: List[Round] = []
    players: List[PlayerId] = []
    time_control: TimeControl
    description: str

    @property
    def is_over(self):
        return self.end_date is not None

    @property
    def played_matches(self) -> List[Match]:
        return [(match for match in rnd.matches if match.played) for rnd in self.rounds]

    @property
    def matches(self) -> List[Match]:
        return [(match for match in rnd.matches) for rnd in self.rounds]

    def get_player_score(self, player_id: PositiveInt):
        score = 0.
        for match in self.played_matches:
            if match.id_player1 == player_id:
                score += match.score_player1
            elif match.id_player2 == player_id:
                score += match.score_player2
        return score

    def generate_match(self, p1, players):
        for p2 in players:
            match = Match(id_player1=p1.id, id_player2=p2.id)
            if match not in self.matches:
                players.pop(players.index(p2))
                return match
        p2 = players.pop(0)
        match = Match(id_player1=p1.id, id_player2=p2.id)
        return match

    def generate_first_round(self, rnd):
        players = sorted([pm.find_by_id(player_id) for player_id in self.players], key=lambda x: (x.rank, x.last_name, x.first_name))
        rnd.matches += [Match(id_player1=a.id, id_player2=b.id) for a, b in zip(players[4:], players[:4])]
        return rnd

    def generate_next_round(self, rnd):
        players = sorted([pm.find_by_id(player_id) for player_id in self.players], key=lambda x: (
            -self.get_player_score(x.id), x.rank))
        while players:
            p1 = players.pop(0)
            match = self.generate_match(p1, players)
            rnd.matches.append(match)
        return rnd

    def generate_round(self, round_name, number_round):
        rnd = Round(name=round_name)
        if number_round == 1:
            return self.generate_first_round(rnd)
        else:
            return self.generate_next_round(rnd)

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
    def check_rounds(cls, value: List[Round]):
        value = [Round(**round_data) for round_data in value]
        return value
