"""Define the main controller."""

from models.player import Player

class Controller:
    """Main controller."""

    def __init__(self, view):
        """Initialize models and views."""
        # Models
        self.players = []

        # Views
        self.view = view
    
    def get_players(self):
        """Get some players."""
        while len(self.players) < 1:
            last_name = self.view.prompt_for_player()
            first_name = self.view.prompt_for_player()
            birth_date = self.view.prompt_for_player()
            sex = self.view.prompt_for_player()
            rank = self.view.prompt_for_player()
            player = Player(last_name, first_name, birth_date, sex, rank)
            self.players.append(player)
    
    def run(self):
        """run the script."""
        self.get_players()