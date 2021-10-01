from utils.view import View


class Error(View):
    """ Permet d'afficher un message d'erreur à l'utilisateur """
    def __init__(self, message):
        super().__init__("Erreur", message, blocking=True)
