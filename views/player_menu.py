from utils.menu import Menu


class PlayerMenu(Menu):
    """Classe représentant le menu de gestion des joueurs."""
    def __init__(self):
        """Permet de construire le menu de gestion des joueurs."""
        super().__init__(
            "Menu de gestion des joueurs",
            [("Ajouter un joueur", "/players/create"),
             ("Lister tous les joueurs", "/players/list/by-name"),
             ("Modifier le classement d'un joueur", "/players/edit"),
             ("Retour", "/")
             ])
