from utils.table import Table
from models.tournament import Tournament
from models.tournament import tournament_manager as tm


class TournamentTable(Table):
    def __init__(self):
        tournaments = tm.find_all()
        super().__init__("Liste des tournois", tournaments)

    def _format_header(self):
        return f"{'#'.ljust(3)} "\
               f"{'Nom'.ljust(20)} "\
               f"{'Lieu'.ljust(20)} "\
               f"{'Date de début'.rjust(5)} "\
               f"{'Date de fin'.rjust(20)} "\
               f"{'Nombre de rounds'.rjust(25)} "

    def _format_item(self, tournament: Tournament):
        return f"{str(tournament.id).ljust(3)} "\
               f"{tournament.name.ljust(20)} "\
               f"{tournament.location.ljust(20)} "\
               f"{tournament.start_date.rjust(10)} "\
               f"{str(tournament.number_rounds).rjust(5)}"

#f"{tournament.end_date.rjust(22)} "\