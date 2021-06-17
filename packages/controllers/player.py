"""Define the main controller."""

from typing import List

from .packages.models.player import Player

class Controller:
    """Main controller."""

    def __init__(self, view):
        """Has a list of players and a view."""
        # models
        self.players: List[Player] = []

        # views
        self.view = view
    
    def get_players(self):
        while len(self.players) < 8:
            player_informations = self.view.prompts_for_manager()
            player = Player(player_informations)
            self.players.append(player)