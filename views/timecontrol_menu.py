from utils.enum_menu import EnumMenu
from utils.custom_types import TimeControl


class TimeControlMenu(EnumMenu):
    """Menu qui permet d'effectuer le choix du type de contrôle du temps d'un tournoi."""
    def __init__(self):
        super().__init__(
            "Sélectionnez le type de contrôle du temps :",
            TimeControl)
