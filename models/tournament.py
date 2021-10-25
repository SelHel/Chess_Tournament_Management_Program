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
    """Modèle représentant un tournoi d'échec."""
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
        """Indique si le tournoi a été terminé."""
        return self.end_date is not None

    @property
    def played_matches(self) -> List[Match]:
        """Retourne uniquement les matchs du tournoi déjà joués."""
        return [(match for match in rnd.matches if match.played) for rnd in self.rounds]

    @property
    def matches(self) -> List[Match]:
        """Retourne tous les matchs du tournoi."""
        return [(match for match in rnd.matches) for rnd in self.rounds]

    def get_player_score(self, player_id: PositiveInt):
        """Retourne le score du joueur passé en paramètre."""
        score = 0.
        for match in self.played_matches:
            if match.id_player1 == player_id:
                score += match.score_player1
            elif match.id_player2 == player_id:
                score += match.score_player2
        return score

    def generate_match(self, p1, players):
        """Génère et retourne un match du tournoi."""
        for p2 in players:
            match = Match(id_player1=p1.id, id_player2=p2.id)
            if match not in self.matches:
                players.pop(players.index(p2))
                return match
        p2 = players.pop(0)
        match = Match(id_player1=p1.id, id_player2=p2.id)
        return match

    def generate_first_round(self, rnd):
        """Génère et retourne le premier round du tournoi."""
        players = sorted([pm.find_by_id(player_id) for player_id in self.players],
                         key=lambda x: (x.rank, x.last_name, x.first_name))
        rnd.matches += [Match(id_player1=a.id, id_player2=b.id) for a, b in zip(players[4:], players[:4])]
        return rnd

    def generate_next_round(self, rnd):
        """Génère et retourne les autres rounds du tournoi."""
        players = sorted([pm.find_by_id(player_id) for player_id in self.players], key=lambda x: (
            -self.get_player_score(x.id), x.rank))
        while players:
            p1 = players.pop(0)
            match = self.generate_match(p1, players)
            rnd.matches.append(match)
        return rnd

    def generate_round(self, round_name, number_round):
        """Génère et retourne un round en fonction de son numéro."""
        rnd = Round(name=round_name)
        if number_round == 1:
            return self.generate_first_round(rnd)
        else:
            return self.generate_next_round(rnd)

    @validator("location", "name")
    def check_len_name(cls, value):
        """Vérifie si le nom entré par l'utilisateur est valide."""
        if len(value) > 35:
            raise ValueError("Le nom ne doit pas dépasser 25 caractères.")
        return value

    # @validator("end_date")
    # def check_dates_match(cls, value, values):
    #     if value < values["start_date"]:
    #         raise ValueError("La date de fin du tournoi doit être supérieure ou égale à la date de début.")
    #     return value

    @validator("players")
    def check_nb_players(cls, value):
        """Vérifie si le nombre de joueurs entré par l'utilisateur est valide."""
        if len(value) < 2 or len(value) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair et supérieur ou égal à 2.")
        return value

    @validator("players")
    def check_players(cls, value):
        """Vérifie si le joueur entré par l'utilisateur n'est pas déjà inscrit dans le tournoi."""
        count = Counter(value)
        for c in dict(count):
            if count[c] > 1:
                raise ValueError("Un joueur ne peut pas s'inscrire plusieurs fois dans un tournoi.")
        for player_id in value:
            pm.find_by_id(player_id)
        return value

    @validator("description")
    def check_description(cls, value):
        """Vérifie si la description entrée par l'utilisateur ne dépasse pas la longueur maximale autorisée."""
        if len(value) > 150:
            raise ValueError("La description du tournoi ne doit pas dépasser 150 caractères.")
        return value

    @validator("rounds")
    def check_rounds(cls, value: List[Round]):
        value = [Round(**round_data) for round_data in value]
        return value
