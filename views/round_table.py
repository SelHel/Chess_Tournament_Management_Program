from typing import List
from utils.table import Table
from models.round import Round


class RoundTable(Table):
    """Classe représentant la table de rounds."""
    def __init__(self, rounds: List[Round]):
        """
        Permet de construire un tableau des rounds.

        Paramètres
        ----------
        rounds: List[Round]
            Liste des rounds de la table
        """
        super().__init__("Liste des tours du tournoi", rounds, [
                ('Nom', 20, lambda x: x.name),
                ('Date de début', 18, lambda x: x.start_time),
                ('Date de fin', 20, lambda x: x.end_time)
            ], [("Retour", "/tournaments")])
