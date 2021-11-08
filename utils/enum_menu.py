from enum import Enum
from utils.menu import Menu


class EnumMenu(Menu):
    """Classe représentant un menu d'énumération."""
    def __init__(self, title: str, enum: Enum, start=1):
        """
        Construit tous les attributs nécessaires à l'objet EnumMenu.

        Paramètres
        ----------
        title : str
            Titre du menu
        enum : Enum
            définit les énumérations
        start : int
            Chiffre de commencement des choix du menu
        """
        choices = [("Retour en arrière.", 0)]
        choices += [(i.value, i) for i in enum]
        super().__init__(title, choices, content="", start=start)
