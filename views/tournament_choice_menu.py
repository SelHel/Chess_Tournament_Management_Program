from typing import List
from models.tournament import Tournament
from utils.menu import Menu


class TournamentChoiceMenu(Menu):
    """Menu qui permet d'effectuer un choix dans la liste de tous les tournois."""
    def __init__(self, tournaments: List[Tournament]):
        super().__init__(
            "Sélectionnez un tournoi dans la liste :",
            [("Retour en arrière", 0)] +
            [(f"{tournament.name}", tournament.id) for tournament in tournaments],
            start=0)
