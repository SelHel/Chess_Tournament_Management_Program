from utils.menu import Menu


class MainMenu(Menu):
    def __init__(self):
        super().__init__(
            "Menu principal",
            [("Gestion des joueurs", "/players"),
             ("Gestion des tournois", "/tournaments"),
             ("Quitter", None)
             ])
