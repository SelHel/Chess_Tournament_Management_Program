from utils.menu import Menu


class PlayerMenu(Menu):
    def __init__(self):
        super().__init__(
            "Menu de gestion des joueurs",
            [("Ajouter un joueur", "/players/create"),
             ("Lister tous les joueurs par classement", "/players/all/rank"),
             ("Lister tous les joueurs par ordre alphabétique", "/players/all/name"),
             ("Modifier le classement d'un joueur", "/players/edit"),
             ("Retour", "/")
             ])
