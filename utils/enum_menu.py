from enum import Enum
from utils.menu import Menu


class EnumMenu(Menu):
    def __init__(self, title: str, enum: Enum):
        choices = [(i.value, i) for i in enum]
        super().__init__(title, choices)
