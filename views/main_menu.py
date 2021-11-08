from utils.menu import Menu


class MainMenu(Menu):
    """Classe représentant le menu principal."""
    def __init__(self):
        """Permet de construire le menu principal."""
        super().__init__(
            "Menu principal",
            [("Gestion des joueurs", "/players"),
             ("Gestion des tournois", "/tournaments"),
             ("Quitter", "/quit")
             ])
