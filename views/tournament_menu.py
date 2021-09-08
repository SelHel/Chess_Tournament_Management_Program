from utils.menu import Menu


class TournamentMenu(Menu):
    def __init__(self):
        super().__init__(
            "Menu de gestion des tournois",
            [("Créer un nouveau tournoi", "/tournaments/create"),
             ("Reprendre un tournoi arrêté", "/tournaments/play"),
             ("Lister tous les tournois", "/tournaments/all"),
             ("Retour", "/")
             ])
