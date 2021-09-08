from datetime import date, datetime
from utils.form import Form
from utils.custom_types import PositiveInt

from views.error import Error
from utils.router import router
from views.player_table import PlayerTable
from views.main_menu import MainMenu
from views.player_menu import PlayerMenu
from views.tournament_table import TournamentTable
from views.tournament_menu import TournamentMenu
from views.player_form import AddPlayerForm, EditPlayerForm
from views.tournament_form import AddTournamentForm, LoadTournamentForm
from models.player import player_manager as pm
from models.tournament import tournament_manager as tm


def main_ctrl():
    router.navigate(MainMenu().display())


def players_ctrl():
    router.navigate(PlayerMenu().display())


def players_create_ctrl():
    data = AddPlayerForm().display()
    data["birth_date"] = date(year=data['bd_year'],
                              month=data['bd_month'],
                              day=data['bd_day']).isoformat()
    data["id"] = pm.max_id + 1
    try:
        pm.create_item(**data)
    except Exception as e:
        Error(f"Impossible de créer le joueur: {str(e)}").display()
    router.navigate("/players")


def players_all_rank_ctrl():
    PlayerTable(sort_by_rank=True).display()
    router.navigate("/players")


def players_all_name_ctrl():
    PlayerTable(sort_by_rank=False).display()
    router.navigate("/players")


def players_edit_ctrl():
    while True:
        form_data = EditPlayerForm().display()
        try:
            player = pm.find_by_id(form_data["id"])
            player.rank = form_data["rank"]
            break
        except KeyError:
            Error("Veuillez saisir un id et un classement valide.").display()
    router.navigate("/players")


def tournaments_ctrl():
    router.navigate(TournamentMenu().display())


def tournaments_create_ctrl():
    data = AddTournamentForm().display()
    data["players"] = []
    data["start_date"] = datetime(year=data['sd_year'],
                                  month=data['sd_month'],
                                  day=data['sd_day'],
                                  hour=data['sd_hour'],
                                  minute=data['sd_minute']).isoformat()
    data["id"] = tm.max_id + 1
    for i in range(data["nb_players"]):
        while True:
            form_data = Form("Ajout d'un joueur", [("id", "Identifiant", PositiveInt)]).display()
            try:
                pm.find_by_id(form_data["id"])
                data["players"].append(form_data["id"])
                break
            except KeyError:
                Error("Veuillez saisir un id de joueur valide.").display()
    try:
        tm.create_item(**data)
    except Exception as e:
        Error(f"Impossible de créer le tournoi: {str(e)}").display()
    router.navigate("/tournaments")


def tournaments_play_ctrl():
    LoadTournamentForm().display()
    router.navigate("/tournaments")


def tournaments_all_ctrl():
    TournamentTable().display()
    router.navigate("/tournaments")
