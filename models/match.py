from pydantic import BaseModel, validator
from .player import player_manager as pm


class Match(BaseModel):
    """Model representing a match of the chess tournament round."""
    id_player1: int
    id_player2: int
    score_player1: float
    score_player2: float

    @validator("id_player1", "id_player2")
    def _check_id(cls, value):
        try:
            pm.find_by_id(value)
        except ValueError:
            raise ValueError(f"L'identifiant {player_id} ne correspond à aucun joueur connu.")
        return value
    
    @validator("score_player1", "score_player2")
    def _check_scores(cls, value):
        if value not in (0.0, 0.5, 1.0):
            raise ValueError("Le score doit être compris entre 0 et 1.")
        return value
    
