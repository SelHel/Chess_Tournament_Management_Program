from typing import List
from utils.table import Table
from models.match import Match
from utils.player_manager import pm


class MatchTable(Table):
    """Classe représentant la table de matchs."""
    def __init__(self, matches: List[Match]):
        """
        Permet de construire un tableau des matchs.

        Paramètres
        ----------
        matches : List[Match]
            La liste des matchs de la table
        """
        super().__init__("Liste des matchs du tournoi", matches, [
            ('Joueur 1', 20, lambda x: str(pm.find_by_id(x.id_player1))),
            ('Joueur 2', 40, lambda x: str(pm.find_by_id(x.id_player2))),
            ('Score Joueur 1', 20, lambda x: x.score_player1),
            ('Score Joueur 2', 30, lambda x: x.score_player2)
            ], [("Retour", "/tournaments")])
