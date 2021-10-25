from typing import List
from models.tournament import Tournament
from utils.menu import Menu


class TournamentChoiceMenu(Menu):
    """Menu qui permet d'effectuer un choix dans la liste de tous les tournois."""
    def __init__(self, tournaments: List[Tournament]):
        super().__init__(
            "Sélectionnez un tournoi dans la liste :",
            [(f"{tournament.name}", tournament.id) for tournament in tournaments])
