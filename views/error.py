from utils.view import View


class Error(View):
    def __init__(self, message):
        super().__init__("Erreur", message, blocking=True)
