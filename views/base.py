"""Base view."""


class View:
    """Manager view."""
    
    def prompt_for_player(self):
        """Prompt for a last name, a first name, a date of birth, a sex and a rank."""
        last_name = input("Entrez le nom de famille du joueur : ")
        first_name = input("Entrez le prénom du joueur : ")
        birth_date = input("Entrez la date de naissance du joueur : ")
        sex = input("Entrez le sexe du joueur : ")
        rank = input("Entrez le classement du joueur : ")