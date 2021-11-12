from typing import Any
from pydantic.main import BaseModel
from utils.custom_types import Score
from utils.player_id import PlayerId


class Match(BaseModel):
    """
    Modèle représentant un match d'un round du tournoi d'échecs.

    Champs obligatoires
    -------------------
    id_player1 : PlayerId
        L'id du premier joueur du match
    id_player2 : PlayerId
        L'id du deuxième joueur du match
    score_player1 : Score
        Le score du premier joueur du match
    score_PLayer2 : Score
        Le score du deuxième joueur du match
    """
    id_player1: PlayerId
    id_player2: PlayerId
    score_player1: Score = Score.UNKNOWN
    score_player2: Score = Score.UNKNOWN

    @property
    def played(self) -> bool:
        """
        Utilisation du décorateur @property pour accéder en tant que propriété à l'état d'un match.
        La méthode played utilise le score du joueur 1 pour vérifier si le match a déjà été joué.

        Retour
        ------
        Retourne True si le score du joueur 1 n'est pas égal à -1.
        Sinon retourne False.
        """
        return self.score_player1 != Score.UNKNOWN

    def __eq__(self, other: Any) -> bool:
        """
        Méthode qui compare l'égalité de deux objets.
        Vérifie si l'objet other est une instance de la classe Match.
        Si oui vérifie si les valeurs de self et de other sont égales.

        Paramètres
        ----------
        other : Any
            valeur de type Any

        Retour
        ------
        Retourne True si other est une instance de Match et si les valeurs des id des joueurs sont égaux,
        sinon retourne False.
        """
        if isinstance(other, Match):
            return tuple(sorted((self.id_player1, self.id_player2))) == tuple(
                sorted((other.id_player1, other.id_player2)))
        return False
