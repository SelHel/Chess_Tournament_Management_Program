from typing import List

from utils.view import View


class Menu(View):
    def __init__(self, title: str, choices: List[str]):
        content = "\n".join([f"{i} - {choice}" for i, choice in enumerate(choices, start=1)])
        super().__init__(title, content, blocking=True)

    def display(self):
        return int(super().display())
