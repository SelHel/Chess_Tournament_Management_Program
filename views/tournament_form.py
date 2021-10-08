from views.timecontrol_menu import TimeControlMenu
from utils.custom_types import PositiveInt
from utils.form import Form


class AddTournamentForm(Form):
    def __init__(self):
        super().__init__(
            "Formulaire de création d'un nouveau tournoi",
            [("name", "Nom du tournoi", str),
             ("location", "Lieu du tournoi", str),
             ("description", "Description du tournoi", str),
             ("number_rounds", "Nombre de tours", PositiveInt),
             ("nb_players", "Saisir le nombre de joueurs", PositiveInt),
             ("time_control", "Contrôle du temps", TimeControlMenu)])


class LoadTournamentForm(Form):
    def __init__(self):
        super().__init__(
            "Formulaire de chargement d'un tournoi arrêté",
            [("id", "Saisir l'id du tournoi", PositiveInt)])
