

class ManagerView:
    """Manager view."""
    def prompt_for_manager(self):
        """Prompt for a last name, a first name, a date of birth, a sex and a rank."""
        last_name = input("saisir le nom de famille du joueur : ")
        first_name = input("saisir le prénom de famille du joueur : ")
        birth_date = input("saisir la date de naissance du joueur : ")
        sex = input("saisir le sexe du joueur : ")
        rank = input("saisir le classement du joueur : ")