from utils.table import Table
from models.player import Player
from models.player import player_manager as pm


class PlayerTable(Table):
    def __init__(self, sort_by_rank: bool = False):
        players = pm.find_all()
        if sort_by_rank:
            players.sort(key=lambda player: (player.rank, player.last_name, player.first_name))
        else:
            players.sort(key=lambda player: (player.last_name, player.first_name, player.rank))
        super().__init__("Liste des joueurs", players)

    def _format_header(self):
        return f"{'#'.ljust(3)} "\
               f"{'Nom'.ljust(20)} "\
               f"{'Prénom'.ljust(20)} "\
               f"{'Date de naissance'} "\
               f"{'Genre'.rjust(15)} "\
               f"{'Rang'.rjust(15)} "

    def _format_item(self, player: Player):
        return f"{str(player.id).ljust(3)} "\
               f"{player.last_name.ljust(20)} "\
               f"{player.first_name.ljust(20)} "\
               f"{player.birth_date} "\
               f"{player.gender.value.rjust(20)} "\
               f"{str(player.rank).rjust(15)}"
