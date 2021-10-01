from utils.enum_menu import EnumMenu
from utils.custom_types import TimeControl


class TimeControlMenu(EnumMenu):
    def __init__(self):
        super().__init__(
            "Sélection du type de contrôle du temps",
            TimeControl)
