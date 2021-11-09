from utils.view import View


class Error(View):
    """Classe représentant une erreur."""
    def __init__(self, message):
        """
        Construit tous les attributs nécessaires à l'objet Erreur.

        Paramètres
        ----------
        message : str
            Message de l'erreur
        """
        super().__init__("Erreur", message, with_input=True)
