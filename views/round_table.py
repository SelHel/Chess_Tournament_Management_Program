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
            La liste des rounds de la table
        """
        super().__init__("Liste des rounds du tournoi", rounds, [
                ('Nom', 10, lambda x: x.name),
                ('Date de début', 40, lambda x: x.start_time),
                ('Date de fin', 40, lambda x: x.end_time)
            ], [("Retour", "/tournaments")])
