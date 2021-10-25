from utils.menu import Menu


class TournamentMenu(Menu):
    def __init__(self):
        super().__init__(
            "Menu de gestion des tournois",
            [("Créer un nouveau tournoi", "/tournaments/create"),
             ("Jouer un tournoi", "/tournaments/play"),
             ("Lister tous les tournois", "/tournaments/list/by-id"),
             ("Lister tous les tours d'un tournoi", "/tournaments/rounds/list"),
             ("Lister tous les matchs d'un tournoi", "/tournaments/matches/list"),
             ("Retour", "/")
             ])
