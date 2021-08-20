from utils.form import Form
from utils.custom_types import Name


class PlayerForm(Form):
    def __init__(self):
        super().__init__(
            "Formulaire d'ajout d'un joueur",
            [("last_name", "Nom de famille du joueur", Name)]
        )
