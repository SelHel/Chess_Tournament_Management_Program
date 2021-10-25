from typing import List
from utils.table import Table
from models.round import Round


class RoundTable(Table):
    """Permet de lister les tours d'un tournoi dans un tableau."""
    def __init__(self, rounds: List[Round]):
        super().__init__("Liste des tours du tournoi", rounds, [
                ('Nom', 20, lambda x: x.name),
                ('Date de début', 18, lambda x: x.start_time),
                ('Date de fin', 20, lambda x: x.end_time)
            ], [("Retour", "/tournaments")])
