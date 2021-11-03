from typing import List, Tuple, Any
from utils.enum_menu import EnumMenu
from utils.view import View


class Form(View):
    """Permet de construire et d'afficher un formulaire."""
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        self.fields = fields
        super().__init__(title)

    def display(self):
        """Permet d'afficher un formulaire, de stocker et de retourner les données entrées par l'utilisateur."""
        data = {}
        super().display()
        for field, description, field_type in self.fields:
            print("----------------------")
            print("0 - Retour en arrière.")
            print("----------------------")
            while True:
                try:
                    if isinstance(field_type(), EnumMenu):
                        data[field] = field_type().display()
                        break
                except TypeError:
                    pass
                try:
                    data[field] = field_type(input(description + " : "))
                    break
                except ValueError:
                    pass
            if data[field] in [0, "0"]:
                return None
        return data
