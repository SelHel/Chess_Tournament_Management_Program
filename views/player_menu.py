from utils.menu import Menu


class PlayerMenu(Menu):
    def __init__(self):
        super().__init__(
            "Menu de gestion des joueurs",
            [("Ajouter un joueur", "/players/create"),
             ("Lister tous les joueurs", "/players/list/by-name"),
             ("Modifier le classement d'un joueur", "/players/edit"),
             ("Retour", "/")
             ])
