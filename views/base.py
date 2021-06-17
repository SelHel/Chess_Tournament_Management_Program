"""Base view."""


class View:
    """Manager view."""
    
    def prompt_for_player(self):
        """Prompt for a name."""
        name = input("Entrez le nom du joueur : ")
        return name
