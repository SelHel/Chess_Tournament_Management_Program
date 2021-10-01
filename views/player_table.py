from typing import List
from utils.table import Table
from models.player import Player


class PlayerTable(Table):
    """ Permet de lister les joueurs """
    def __init__(self, players: List[Player], sorting: str):
        inv_sorting = "by-name" if sorting == "by-rank" else "by-rank"
        super().__init__("Liste des joueurs", sorted(
            players, key=lambda x: (
                (x.rank, x.last_name, x.first_name) if sorting == "by-rank"
                else (x.last_name, x.first_name, x.rank))
            ), [
                ("#", 3, lambda x: x.id),
                ("Nom", 15, lambda x: x.last_name),
                ("Prénom", 15, lambda x: x.first_name),
                ("Date de naissance", 20, lambda x: x.birth_date.strftime("%d/%m/%Y")),
                ("Sexe", 4, lambda x: x.gender.name),
                ("Rang", 5, lambda x: x.rank)
            ], [(f"Trier par {'nom' if inv_sorting == 'by-name' else 'classement'}", f"/players/list/{inv_sorting}"),
                ("Retour", "/players")
                ])