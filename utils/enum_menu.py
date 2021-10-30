from enum import Enum
from utils.menu import Menu


class EnumMenu(Menu):
    """Permet de construire un menu à partir d'une classe de type Enum."""
    def __init__(self, title: str, enum: Enum, start=1):
        choices = [("Retour en arrière.", 0)]
        choices += [(i.value, i) for i in enum]
        super().__init__(title, choices, content="", start=start)
