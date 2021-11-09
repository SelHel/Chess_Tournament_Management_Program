from datetime import date
from pydantic import BaseModel, PositiveInt, validator
from utils.custom_types import Name, Gender


class Player(BaseModel):
    """
    Modèle représentant un joueur du tournoi d'échecs.

    Champs obligatoires
    -------------------
    id: Positiveint
        L'id du joueur
    last_name : Name
        Le nom de famille du joueur
    first_name : Name
        Le prénom du joueur
    birth_date : date
        La date de naissance du joueur
    gender : Gender
        Le genre du joueur
    rank : PositiveInt
        Le classement du joueur
    """
    id: PositiveInt
    last_name: Name
    first_name: Name
    birth_date: date
    gender: Gender
    rank: PositiveInt

    def __str__(self) -> str: 
        """
        Méthode spéciale qui permet la représentation en chaîne de caractères de l'objet Player.

        Retour
        ------
            Retourne le Nom et Prénom du joueur.
        """
        return f"{self.last_name} {self.first_name}"

    @validator("birth_date")
    def check_player_age(cls, value):
        """
        Utilisation du décorateur @validator pour définir la méthode check_player_age.
        Méthode de validation du champs birth_date.
        Vérifie en fonction de la date de naissance du joueur si celui-ci à l'âge minimum requis.

        Paramètres
        ----------
        cls : UserModel classe
            La classe Player
        value : la valeur du champ à valider
            Le champs birth_date

        Retour
        ------
        Retourne la valeur analysée ou lève une ValueError.
        """
        today = date.today()
        player_age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if player_age < 16:
            raise ValueError("Le joueur doit avoir au minimum 16 ans.")
        return value
