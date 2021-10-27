from typing import Any
from pydantic.main import BaseModel
from utils.custom_types import Score
from utils.player_id import PlayerId


class Match(BaseModel):
    """Modèle représentant un match d'un round du tournoi d'échecs."""
    id_player1: PlayerId
    id_player2: PlayerId
    score_player1: Score = Score.UNKNOWN
    score_player2: Score = Score.UNKNOWN

    @property
    def winner(self) -> str:
        """Retourne le résultat du match."""
        if self.score_player1 == Score.UNKNOWN:
            return "Match non joué"
        if self.score_player1 == Score.WIN:
            return "Joueur 1"
        if self.score_player1 == Score.LOSE:
            return "Joueur 2"
        if self.score_player1 == Score.DRAW:
            return "Égalité"

    @property
    def played(self) -> bool:
        """Indique si le match a déjà été joué."""
        return self.score_player1 + self.score_player2 == 1.0

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Match):
            return tuple(sorted((self.id_player1, self.id_player2))) == tuple(
                sorted((other.id_player1, other.id_player2)))
        return False
