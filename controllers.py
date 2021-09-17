from datetime import date, datetime

from utils.router import router
from views.error import Error
from views.player_table import PlayerTable
from views.main_menu import MainMenu
from views.player_menu import PlayerMenu
from views.tournament_table import TournamentTable
from views.tournament_menu import TournamentMenu
from views.player_form import AddPlayerForm, EditPlayerForm
from views.tournament_form import AddTournamentForm, LoadTournamentForm
from views.playerchoice_menu import PlayerChoiceMenu
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
    router.navigate(PlayerTable(pm.find_all(), sorting="by-rank").display())


def players_all_name_ctrl():
    router.navigate(PlayerTable(pm.find_all(), sorting="by-name").display())


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
    data["id"] = tm.max_id + 1
    data["players"] = []
    data["start_date"] = datetime.today()
    players = pm.find_all()
    for i in range(data["nb_players"]):
        player_id = PlayerChoiceMenu(players).display()
        data["players"].append(player_id)
        players = [player for player in players if player_id != player.id]
    try:
        input(data)
        tm.create_item(**data)
    except Exception as e:
        Error(f"Impossible de créer le tournoi: {str(e)}").display()
    router.navigate("/tournaments")


def tournaments_play_ctrl():
    LoadTournamentForm().display()
    router.navigate("/tournaments")


def tournaments_all_ctrl():
    TournamentTable(tm.find_all()).display()
    router.navigate("/tournaments")
