from typing import List, Tuple
from utils.view import View


class Menu(View):
    """Permet de construire un menu."""
    def __init__(self, title: str, choices: List[Tuple[str, str]], content="", start=1):
        self.start = start
        self.paths = [path for _, path in choices]
        content = content + "\n" + "\n".join([f"{i} - {choice}" for i, (choice, _) in enumerate(choices, start=start)])
        super().__init__(title, content, blocking=True)

    def display(self):
        """Méthode permettant d'afficher un menu et retourne le choix effectué par l'utilisateur."""
        while True:
            try:
                choice = int(super().display())
                if self.start <= choice < len(self.paths) + self.start:
                    return self.paths[choice - self.start]
            except ValueError:
                pass
