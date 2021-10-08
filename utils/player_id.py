from .player_manager import pm


class PlayerId(int):
    def __new__(cls, value: int):
        try:
            pm.find_by_id(value)
        except ValueError:
            raise ValueError("L'identifiant ne correspond à aucun joueur connu.")
        return super().__new__(cls, value)
