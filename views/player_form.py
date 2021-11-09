from utils.custom_types import PositiveInt
from utils.form import Form
from utils.custom_types import Name, Gender


class AddPlayerForm(Form):
    """Classe représentant le formulaire d'ajout d'un joueur."""
    def __init__(self):
        """Permet de construire le formulaire d'ajout d'un joueur."""
        super().__init__(
            "Formulaire d'ajout d'un joueur",
            [("last_name", "Nom de famille du joueur", Name),
             ("first_name", "Prénom du joueur", Name),
             ("bd_year", "Année de naissance du joueur", PositiveInt),
             ("bd_month", "Mois de naissance du joueur", PositiveInt),
             ("bd_day", "Jour de naissance du joueur", PositiveInt),
             ("gender", "Genre du joueur (F/M)", Gender),
             ("rank", "Classement du joueur", PositiveInt)])


class EditPlayerForm(Form):
    """Classe représentant le formulaire permettant la modification du classement d'un joueur."""
    def __init__(self):
        """Permet de construire le formulaire de modification du classement d'un joueur."""
        super().__init__(
            "Formulaire de mise à jour du classement d'un joueur",
            [("rank", "Saisissez le nouveau classement du joueur sélectionné ", PositiveInt)])
