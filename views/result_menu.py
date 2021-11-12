from utils.menu import Menu
from models.player import Player
from models.round import Round


class ResultMenu(Menu):
    """Classe représentant le menu permettant d'effectuer le choix du résultat d'un match."""
    def __init__(self, player1: Player, player2: Player, round: Round):
        """
        Permet de construire le menu de choix du résultat d'un match.

        Paramètres
        ----------
        player1: Player
            Le premier joueur du match
        player2: Player
            Le deuxième joueur du match
        round: Round
            Le round du tournoi
        """
        super().__init__(
            f"{round.name}\n---------\nSélectionnez le résultat du match :",
            [(f"{player1.first_name} {player1.last_name} a gagné.", 1.0),
                (f"{player2.first_name} {player2.last_name} a gagné.", 0.0),
                ("Les joueurs sont à égalité.", 0.5)]
            + [("Retour en arrière", 4)])
