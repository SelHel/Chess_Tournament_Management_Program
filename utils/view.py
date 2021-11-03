import os


class View:
    """Définition d'une vue."""
    def __init__(self, title: str, content: str = "", blocking: bool = False):
        self.title = title
        self.content = content
        self.blocking = blocking

    def display(self):
        os.system("clear")
        print(self.title)
        print("-" * len(self.title))
        if self.content:
            if not self.blocking:
                print(self.content)
            else:
                return input(self.content + "\n: ")
