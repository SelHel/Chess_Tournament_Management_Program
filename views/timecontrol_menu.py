from utils.enum_menu import EnumMenu
from utils.custom_types import TimeControl


class TimeControlMenu(EnumMenu):
    """Classe représentant le menu de sélection du type de contrôle du temps d'un tournoi."""
    def __init__(self):
        """Permet de construire le menu de sélection du type de contrôle du temps d'un tournoi."""
        super().__init__(
            "Sélectionnez le type de contrôle du temps :",
            TimeControl, start=0)
