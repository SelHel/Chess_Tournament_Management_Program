import sys
from datetime import date, datetime
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
from utils.custom_types import Score

"""Les contrôleurs garantissent que les commandes utilisateurs soient exécutées correctement."""


def main_ctrl():
    """Renvoie l'utilisateur au menu principal."""
    router.navigate(MainMenu().display())


def players_ctrl():
    """Renvoie l'utilisateur au menu de gestion des joueurs."""
    router.navigate(PlayerMenu().display())


def tournaments_ctrl():
    """Renvoie l'utilisateur au menu de gestion des tournois."""
    router.navigate(TournamentMenu().display())


def quit_ctrl():
    """Permet de quitter l'application."""
    sys.exit()


def players_create_ctrl():
    """
    Affiche le formulaire d'ajout d'un joueur.
    Récupère les données entrées par l'utilisateur puis essaie de créé l'objet ou lève une erreur.
    Une fois le formulaire complété renvoie l'utilisateur au menu de gestion des joueurs.
    """
    data = AddPlayerForm().display()
    if data:
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
    """Affiche la table des joueurs trier par classement."""
    router.navigate(PlayerTable(pm.find_all(), sorting="by-rank").display())


def players_all_name_ctrl():
    """Affiche la table des joueurs trier par noms."""
    router.navigate(PlayerTable(pm.find_all(), sorting="by-name").display())


def players_edit_ctrl():
    """
    Affiche le menu permettant d'effectuer un choix dans la liste de tous les joueurs.
    Récupère le joueur choisit par l'utilisateur.
    Renvoie l'utilisateur au formulaire de modification du classement du joueur.
    Récupère le nouveau classement du joueur, effectue une sauvegarde puis
    renvoie l'utilisateur au menu de gestion des joueurs.
    """
    while True:
        players = pm.find_all()
        player_id = PlayerChoiceMenu(players).display()
        if player_id == 0:  # Si l'utilisateur choisit "Retourner en arriere", le player_id sera égal 0.
            return router.navigate("/players")
        try:
            player = pm.find_by_id(player_id)
            player_str = f"Joueur {player.id}: {player.first_name} {player.last_name} Classement: {player.rank}"
            rank = EditPlayerForm(player_str).display()
            if not rank:  # Si l'utilisateur choisit "Retourner en arriere", le rank sera None.
                return router.navigate("/players")
            player.rank = rank["rank"]
            pm.save_item(player.id)
            break
        except KeyError:
            Error("Veuillez saisir un id et un classement valide.").display()
    router.navigate("/players")


def tournaments_create_ctrl():
    """
    Affiche le formulaire d'ajout d'un tournoi.
    Récupère les données entrées par l'utilisateur puis essaie de créé l'objet ou lève une erreur.
    Une fois le formulaire complété renvoie l'utilisateur au menu de gestion des tournois.
    """
    data = AddTournamentForm().display()
    if data:
        data["id"] = tm.max_id + 1
        data["players"] = []
        players = pm.find_all()
        for i in range(data["nb_players"]):
            player_id = PlayerChoiceMenu(players).display()
            if player_id == 0:  # Si l'utilisateur choisit "Retourner en arriere", le player_id sera égal 0.
                return router.navigate("/tournaments")
            data["players"].append(player_id)
            players = [player for player in players if player_id != player.id]
        try:
            tm.create_item(**data)
        except Exception as e:
            Error(f"Impossible de créer le tournoi: {str(e)}").display()
    router.navigate("/tournaments")


def tournaments_play_ctrl():
    """
    Affiche le menu permettant d'effectuer un choix dans la liste des tournois non terminés.
    Joue chaque match de chaque round du tournoi et affiche le menu permettant d'effectuer le choix
    du résultat d'un match à chaque fin de match.
    Chaque round terminé est sauvegardé et l'utilisateur peut reprendre un tournoi là où il a été arrêté.
    Une fois le tournoi terminé il est sauvegardé puis l'utilisateur est renvoyé au menu de gestion des tournois.
    """
    while True:
        all_tournaments = tm.find_all()
        tournaments = [i for i in all_tournaments if not i.is_over]
        tournament_id = TournamentChoiceMenu(tournaments).display()
        if tournament_id == 0:  # Si l'utilisateur choisit "Retourner en arriere", le tournament_id sera égal 0.
            return router.navigate("/tournaments")
        try:
            tournament = tm.find_by_id(tournament_id)
            for nb_rnd in range(1, tournament.number_rounds + 1):
                if nb_rnd <= len(tournament.rounds):
                    continue
                rnd = tournament.generate_round(f"Round {nb_rnd}", nb_rnd)
                rnd.start_time = datetime.now()
                for match in rnd.matches:
                    result_p1 = ResultMenu(pm.find_by_id(match.id_player1),
                                           pm.find_by_id(match.id_player2), rnd).display()
                    if result_p1 == 4:  # Si l'utilisateur choisit "Retourner en arriere", le result_p1 sera égal 4.
                        return router.navigate("/tournaments")
                    result_p2 = 1 - result_p1
                    match.score_player1 = Score(result_p1)
                    match.score_player2 = Score(result_p2)
                rnd.end_time = datetime.now()
                tournament.rounds.append(rnd)
                tm.save_item(tournament.id)
            tournament.end_date = date.today()
            tm.save_item(tournament.id)
            break
        except KeyError:
            Error("Veuillez saisir un id de tournoi valide.").display()
    router.navigate("/tournaments")


def tournaments_all_ctrl():
    """
    Affiche la table des tournois.
    Puis renvoie l'utilisateur au menu de gestion des tournois.
    """
    TournamentTable(tm.find_all()).display()
    router.navigate("/tournaments")


def tournaments_rounds_ctrl():
    """
    Affiche le menu permettant d'effectuer un choix dans la liste de tous les tournois.
    Affiche la table des rounds du tournoi sélectionné.
    Puis renvoie l'utilisateur au menu de gestion des tournois.
    """
    tournaments = tm.find_all()
    tournament_id = TournamentChoiceMenu(tournaments).display()
    if tournament_id == 0:  # Si l'utilisateur choisit "Retourner en arriere", tournament_id sera égal 0.
        return router.navigate("/tournaments")
    try:
        tournament = tm.find_by_id(tournament_id)
        RoundTable(tournament.rounds).display()
        router.navigate("/tournaments")
    except KeyError:
        Error("Veuillez saisir un id de tournoi valide.").display()


def tournaments_matches_ctrl():
    """
    Affiche le menu permettant d'effectuer un choix dans la liste de tous les tournois.
    Affiche la table des matchs de tous les matchs du tournoi sélectionné.
    Puis renvoie l'utilisateur au menu de gestion des tournois.
    """
    tournaments = tm.find_all()
    tournament_id = TournamentChoiceMenu(tournaments).display()
    if tournament_id == 0:  # Si l'utilisateur choisit "Retourner en arriere", le tournament_id sera égal 0.
        return router.navigate("/tournaments")
    try:
        tournament = tm.find_by_id(tournament_id)
        for round in tournament.rounds:
            MatchTable(round.matches).display()
        router.navigate("/tournaments")
    except KeyError:
        Error("Veuillez saisir un id de tournoi valide.").display()
