from typing import List
from utils.table import Table
from models.tournament import Tournament


class TournamentTable(Table):
    """Classe représentant la table de tournois."""
    def __init__(self, tournaments: List[Tournament]):
        """
        Permet de construire la table des tournois.

        Paramètres
        ----------
        tournaments : List[Tournament]
            La liste des tournois de la table
        """
        super().__init__("Liste des tournois", sorted(
            tournaments, key=lambda x: ((x.id))
            ), [
                ('#', 10, lambda x: x.id),
                ('Nom', 30, lambda x: x.name),
                ('Lieu', 20, lambda x: x.location),
                ('Date de début', 20, lambda x: x.start_date.strftime("%d/%m/%Y")),
                ('Date de fin', 20, lambda x: x.end_date.strftime("%d/%m/%Y") if x.end_date else "-"),
                ('Nombre de rounds', 20, lambda x: x.number_rounds)
            ], [("Retour", "/tournaments")])
