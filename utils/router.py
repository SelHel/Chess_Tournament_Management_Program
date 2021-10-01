from typing import Callable


class Router:
    """ Permet de naviguer entre les menus """
    def __init__(self):
        self.routes = []

    def navigate(self, path: str):
        print(path)
        if path is None:
            return
        for p, ctrl in self.routes:
            if p == path:
                ctrl()

    def add_route(self, path: str, controller: Callable):
        self.routes.append((path, controller))


router = Router()
