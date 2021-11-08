from typing import List, Tuple, Any
from utils.enum_menu import EnumMenu
from utils.view import View


class Form(View):
    """Classe représentant un formulaire."""
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        """
        Construit tous les attributs nécessaires à l'objet Form.

        Paramètres
        ----------
        title : str
            Titre du formulaire
        fields : List[Tuple[str, str, Any]
            Champs du formulaire
        """
        self.fields = fields
        super().__init__(title)

    def display(self):
        """
        Méthode permettant d'afficher un formulaire.

        Retour
        ------
        Retourne les données du formulaire entrées par l'utilisateur.
        """
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
