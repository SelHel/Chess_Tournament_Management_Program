from typing import List
from utils.table import Table
from models.match import Match
from utils.player_manager import pm


class MatchTable(Table):
    """Permet de lister tous les matchs d'un tournoi dans un tableau."""
    def __init__(self, matches: List[Match]):
        super().__init__("Liste des matchs du tournoi", matches, [
            ('Joueur 1', 20, lambda x: str(pm.find_by_id(x.id_player1))),
            ('Joueur 2', 20, lambda x: str(pm.find_by_id(x.id_player2))),
            ('Gagnant', 18, lambda x: x.winner)
            ], [("Retour", "/tournaments")])
