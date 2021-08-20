from utils.router import router
from views.player_table import PlayerTable
from views.main_menu import MainMenu
from views.player_menu import PlayerMenu
from views.tournament_menu import TournamentMenu
from views.player_form import PlayerForm


def main_ctrl():
    router.navigate(MainMenu().display())


def players_ctrl():
    router.navigate(PlayerMenu().display())


def players_create_ctrl():
    PlayerForm().display()
    router.navigate("/players")


def players_all_rank_ctrl():
    PlayerTable(sort_by_rank=True).display()
    router.navigate("/players")


def players_all_name_ctrl():
    PlayerTable(sort_by_rank=False).display()
    router.navigate("/players")


def players_edit_ctrl():
    router.navigate("/players")


def tournaments_ctrl():
    router.navigate(TournamentMenu().display())


def tournaments_create_ctrl():
    router.navigate("/tournaments")


def tournaments_play_ctrl():
    router.navigate("/tournaments")


def tournaments_all_ctrl():
    router.navigate("/tournaments")
