from typing import Any
from pydantic.main import BaseModel
from utils.custom_types import Score
from utils.player_id import PlayerId


class Match(BaseModel):
    """ Modèle représentant un match d'un round du tournoi d'échecs """
    id_player1: PlayerId
    id_player2: PlayerId
    score_player1: Score = Score.UNKNOWN
    score_player2: Score = Score.UNKNOWN

    @property
    def played(self) -> bool:
        return self.score_player1.value + self.score_player2.value == 1.0

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Match):
            return tuple(sorted((self.id_player1, self.id_player2))) == tuple(
                sorted((other.id_player1, other.id_player2)))
        return False
