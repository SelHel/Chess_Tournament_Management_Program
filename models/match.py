from pydantic import BaseModel, validator
from .player import player_manager as pm


class Match(BaseModel):
    """ Modèle représentant un match du round du tournoi d'échecs """
    id_player1: int
    id_player2: int
    score_player1: float = 0.5
    score_player2: float = 0.5

    @validator("id_player1", "id_player2")
    def check_id(cls, value):
        try:
            pm.find_by_id(value)
        except ValueError:
            raise ValueError("L'identifiant ne correspond à aucun joueur connu.")
        return value

    @validator("score_player1", "score_player2")
    def check_scores(cls, value):
        if value not in (0.0, 0.5, 1.0):
            raise ValueError("Le score du joueur doit être 0.0, 0.5 ou 1.0")
        return value
