from .player_manager import pm


class PlayerId(int):
    """Classe représentant l'id d'un joueur."""
    def __new__(cls, value: int):
        """
        La méthode __new__ est appelée avant la création d'un objet PlayerId,
        elle vérifie si la valeur passée en paramètre correspond à l'id d'un joueur connu.

        Paramètres
        ----------
        cls : la classe PlayerId

        value : int
            L'id d'un joueur
        Retour
        ------
        Retourne l'objet nouvellement créé ou lève une ValueError.
        """
        try:
            pm.find_by_id(value)
        except ValueError:
            raise ValueError("L'identifiant ne correspond à aucun joueur connu.")
        return super().__new__(cls, value)
