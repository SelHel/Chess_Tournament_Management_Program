from utils.menu import Menu
from models.player import Player
from models.round import Round


class ResultMenu(Menu):
    """Menu qui permet d'effectuer le choix du résultat d'un match."""
    def __init__(self, player1: Player, player2: Player, round: Round):
        super().__init__(
            f"{round.name}\n---------\nSélectionnez le résultat du match :",
            [(f"{player1.first_name} {player1.last_name} a gagné.", 1.0),
                (f"{player2.first_name} {player2.last_name} a gagné.", 0.0),
                ("Les joueurs sont à égalité.", 0.5)])
