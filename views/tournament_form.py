from views.timecontrol_menu import TimeControlMenu
from utils.custom_types import PositiveInt
from utils.form import Form


class AddTournamentForm(Form):
    """"Formulaire permettant la création d'un tournoi."""
    def __init__(self):
        super().__init__(
            "Formulaire d'ajout d'un nouveau tournoi",
            [("name", "Nom du tournoi", str),
             ("location", "Lieu du tournoi", str),
             ("description", "Description du tournoi", str),
             ("number_rounds", "Nombre de tours", PositiveInt),
             ("nb_players", "Saisir le nombre de joueurs", PositiveInt),
             ("time_control", "Contrôle du temps", TimeControlMenu)])
