from typing import Callable


class Router:
    """Classe représentant un routeur qui permet de naviguer entre les menus du programme."""
    def __init__(self):
        """
        Construit les routes.
        Chaque route représente un tuple qui associe une adresse à une fonction
        qui garantit que les commandes utilisateurs soient exécutées correctement.
        exemple : ("/players/list/by-rank", players_all_rank_ctrl)
        """
        self.routes = []

    def navigate(self, path: str):
        """
        Méthode permettant de naviguer entre les différents menus.

        Paramètres
        ----------
        path : str
            Adresse de destination
        """
        if path is None:
            return
        for p, ctrl in self.routes:
            if p == path:
                ctrl()

    def add_route(self, path: str, controller: Callable):
        """
        Méthode permettant d'ajouter une route au routeur.

        Paramètres
        ----------
        path : str
            Adresse de destination
        controller : Callable
            Le contrôleur (la fonction associée à l'adresse)
        """
        self.routes.append((path, controller))


router = Router()
