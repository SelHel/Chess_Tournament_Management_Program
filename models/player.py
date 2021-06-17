"""Player."""

class Player:
    """Model representing a player."""

    def __init__(self, last_name, first_name, birth_date, sex, rank):
        """Initializes player details."""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
    
    def __str__(self):
        """Used in print."""
        return f"Informations du joueur, Nom : {self.last_name}, Prénom : {self.first_name}, Date de naissance : {self.birth_date}, Sexe : {self.sex}, Classement = {self.rank}"