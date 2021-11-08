from views.timecontrol_menu import TimeControlMenu
from utils.custom_types import PositiveInt
from utils.form import Form


class AddTournamentForm(Form):
    """Classe représentant le formulaire d'ajout d'un tournoi."""
    def __init__(self):
        """Permet de construire le formulaire d'ajout d'un tournoi."""
        super().__init__(
            "Formulaire d'ajout d'un nouveau tournoi",
            [("name", "Nom du tournoi", str),
             ("location", "Lieu du tournoi", str),
             ("description", "Description du tournoi", str),
             ("number_rounds", "Nombre de rounds", PositiveInt),
             ("nb_players", "Saisir le nombre de joueurs", PositiveInt),
             ("time_control", "Contrôle du temps", TimeControlMenu)])
