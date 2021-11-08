from typing import Callable


class Router:
    """Classe représentant un routeur."""
    def __init__(self):
        """Construit le routeur."""
        self.routes = []

    def navigate(self, path: str):
        """
        Méthode permettant de naviguer entre les différents menus.

        Paramètres
        ----------
        path : str
            Chemin du routeur
        """
        if path is None:
            return
        for p, ctrl in self.routes:
            if p == path:
                ctrl()

    def add_route(self, path: str, controller: Callable):
        """
        Méthode permettant d'ajouter un chemin au routeur.

        Paramètres
        ----------
        path : str
            Chemin du routeur
        controller : Callable
            Contrôleur du routeur
        """
        self.routes.append((path, controller))


router = Router()
