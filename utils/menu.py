from typing import List, Tuple
from utils.view import View


class Menu(View):
    def __init__(self, title: str, choices: List[Tuple[str, str]], content=""):
        self.paths = [path for _, path in choices]
        content = content + "\n" + "\n".join([f"{i} - {choice}" for i, (choice, _) in enumerate(choices, start=1)])
        super().__init__(title, content, blocking=True)

    def display(self):
        while True:
            try:
                choice = int(super().display())
                if 0 < choice <= len(self.paths):
                    return self.paths[choice - 1]
            except ValueError:
                pass
