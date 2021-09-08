from utils.custom_types import PositiveInt

from utils.form import Form


class AddTournamentForm(Form):
    def __init__(self):
        super().__init__(
            "Formulaire de création d'un nouveau tournoi",
            [("name", "Nom du tournoi", str),
             ("location", "Lieu du tournoi", str),
             ("sd_year", "Date début du tournoi, Année", PositiveInt),
             ("sd_month", "Mois", PositiveInt),
             ("sd_day", "Jour", PositiveInt),
             ("sd_hour", "Heure", PositiveInt),
             ("sd_minute", "Minutes", PositiveInt),
             ("number_rounds", "Nombre de tours", PositiveInt),
             ("nb_players", "Nombre de joueurs", PositiveInt),
             ("time_control", "Contrôle du temps (bullet, blitz ou coup rapide)", str),
             ("description", "Description du tournoi", str)
             ])


class LoadTournamentForm(Form):
    def __init__(self):
        super().__init__(
            "Formulaire de chargement d'un tournoi arrêté",
            [("id", "Saisir l'id du tournoi", PositiveInt)])
