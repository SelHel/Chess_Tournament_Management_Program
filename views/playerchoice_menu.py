from typing import List
from models.player import Player
from utils.menu import Menu


class PlayerChoiceMenu(Menu):
    def __init__(self, players: List[Player]):
        super().__init__(
            "Menu de sélection des joueurs du tournoi",
            [(f"{player.first_name} {player.last_name}", player.id) for player in players])
