import sys
from datetime import date
from views.match_table import MatchTable
from views.result_menu import ResultMenu
from utils.router import router
from views.error import Error
from views.player_table import PlayerTable
from views.main_menu import MainMenu
from views.player_menu import PlayerMenu
from views.round_table import RoundTable
from views.tournament_choice_menu import TournamentChoiceMenu
from views.tournament_table import TournamentTable
from views.tournament_menu import TournamentMenu
from views.player_form import AddPlayerForm, EditPlayerForm
from views.tournament_form import AddTournamentForm
from views.player_choice_menu import PlayerChoiceMenu
from utils.player_manager import pm
from utils.tournament_manager import tm


def main_ctrl():
    """Renvoie l'utilisateur sur le menu principal."""
    router.navigate(MainMenu().display())


def players_ctrl():
    """Renvoie l'utilisateur sur le menu de gestion des joueurs."""
    router.navigate(PlayerMenu().display())


def tournaments_ctrl():
    """Renvoie l'utilisateur sur le menu de gestion des tournois."""
    router.navigate(TournamentMenu().display())


def quit_ctrl():
    """Permet de quitter l'application."""
    sys.exit()


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
        players = pm.find_all()
        player_id = PlayerChoiceMenu(players).display()
        try:
            player = pm.find_by_id(player_id)
            rank = EditPlayerForm().display()
            player.rank = rank["rank"]
            pm.save_item(player.id)
            break
        except KeyError:
            Error("Veuillez saisir un id et un classement valide.").display()
    router.navigate("/players")


def tournaments_create_ctrl():
    data = AddTournamentForm().display()
    data["id"] = tm.max_id + 1
    data["players"] = []
    players = pm.find_all()
    for i in range(data["nb_players"]):
        player_id = PlayerChoiceMenu(players).display()
        data["players"].append(player_id)
        players = [player for player in players if player_id != player.id]
    try:
        tm.create_item(**data)
    except Exception as e:
        Error(f"Impossible de créer le tournoi: {str(e)}").display()
    router.navigate("/tournaments")


def tournaments_play_ctrl():
    while True:
        tournaments = tm.find_all()
        tournament_id = TournamentChoiceMenu(tournaments).display()
        try:
            tournament = tm.find_by_id(tournament_id)
            for nb_rnd in range(1, tournament.number_rounds + 1):
                rnd = tournament.generate_round(f"Round {nb_rnd}", nb_rnd)
                for match in rnd.matches:
                    result_p1 = ResultMenu(pm.find_by_id(match.id_player1), pm.find_by_id(match.id_player2)).display()
                    result_p2 = 1 - result_p1
                    match.score_player1 = result_p1
                    match.score_player2 = result_p2
                tournament.rounds.append(rnd)
                tm.save_item(tournament.id)
            break
        except KeyError:
            Error("Veuillez saisir un id de tournoi valide.").display()
    router.navigate("/tournaments")


def tournaments_all_ctrl():
    TournamentTable(tm.find_all()).display()
    router.navigate("/tournaments")


def tournaments_rounds_ctrl():
    tournaments = tm.find_all()
    tournament_id = TournamentChoiceMenu(tournaments).display()
    try:
        tournament = tm.find_by_id(tournament_id)
        RoundTable(tournament.rounds)
    except KeyError:
        Error("Veuillez saisir un id de tournoi valide.").display()


def tournaments_matches_ctrl():
    tournaments = tm.find_all()
    tournament_id = TournamentChoiceMenu(tournaments).display()
    try:
        tournament = tm.find_by_id(tournament_id)
        MatchTable(tournament.matches)
    except KeyError:
        Error("Veuillez saisir un id de tournoi valide.").display()
