from typing import List
from models.player import Player
from utils.menu import Menu


class PlayerChoiceMenu(Menu):
    """Menu qui permet d'effectuer un choix dans la liste de tous les joueurs."""
    def __init__(self, players: List[Player]):
        super().__init__(
            "Sélectionnez un joueur dans la liste :",
            [(f"{player.first_name} {player.last_name}", player.id) for player in players])
