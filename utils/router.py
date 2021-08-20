from typing import Callable


class Router:
    def __init__(self):
        self.routes = []

    def navigate(self, path: str):
        if path is None:
            return
        for p, ctrl in self.routes:
            if p == path:
                ctrl()

    def add_route(self, path: str, controller: Callable):
        self.routes.append((path, controller))


router = Router()
