from typing import List, Tuple
from utils.view import View


class Menu(View):
    """Classe représentant un menu."""
    def __init__(self, title: str, choices: List[Tuple[str, str]], content="", start=1):
        """
        Construit tous les attributs nécessaires à l'objet Menu.

        Paramètres
        ----------
        title : str
            Le titre du menu
        choices : List[Tuple[str, str]]
            La liste des choix du menu
        content : str, facultatif
            Le contenu du menu
        start : int
            Le chiffre de commencement des choix du menu
        """
        self.start = start
        self.paths = [path for _, path in choices]
        content = content + "\n" + "\n".join([f"{i} - {choice}" for i, (choice, _) in enumerate(choices, start=start)])
        super().__init__(title, content, with_input=True)

    def display(self):
        """
        Méthode permettant d'afficher un menu.

        Retour
        ------
        Retourne les choix du menu ou lève une ValueError.
        """
        while True:
            try:
                choice = int(super().display())
                if self.start <= choice < len(self.paths) + self.start:
                    return self.paths[choice - self.start]
            except ValueError:
                pass
