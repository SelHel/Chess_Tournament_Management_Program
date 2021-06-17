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
        while len(self.players) < 8:
            name = self.view.prompt_for_player()
            player = Player(name)
            self.players.append(player)
    
    def run(self):
        """Run the script."""
        self.get_players()