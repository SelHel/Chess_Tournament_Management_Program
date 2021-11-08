from typing import List
from models.player import Player
from utils.menu import Menu


class PlayerChoiceMenu(Menu):
    """Classe représentant le menu permettant d'effectuer un choix dans la liste de tous les joueurs."""
    def __init__(self, players: List[Player]):
        """
        Permet de construire le menu de choix des joueurs.

        Paramètres
        ----------
        players : List[Player]
            Liste des joueurs
        """
        super().__init__(
            "Sélectionnez un joueur dans la liste :",
            [("Retour en arrière", 0)] +
            [(f"{player.first_name} {player.last_name}", player.id) for player in players],
            start=0)
