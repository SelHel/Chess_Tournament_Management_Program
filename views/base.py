"""Base view."""


class View:
    """View that manages the user interface."""
    
    def prompt_for_player(self):
        """Prompt for a name."""
        name = input("Entrez le nom du joueur : ")
        return name
    
    def prompt_for_rank(self):
        """Prompt for a rank."""
        rank = input("Entrez le classement du joueur : ")
        return rank



