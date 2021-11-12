from typing import List
from datetime import date
from collections import Counter
from pydantic import BaseModel, PositiveInt, validator
from models.match import Match
from .round import Round
from utils.custom_types import TimeControl
from utils.player_manager import pm
from utils.player_id import PlayerId


class Tournament(BaseModel):
    """
    Modèle représentant un tournoi d'échec.

    Champs obligatoires
    -------------------
    id : PositiveInt
        L'id du tournoi
    name : str
        Le nom du tournoi
    location : str
        Le lieu du tournoi
    start_date : date
        La date de début du tournoi
    end_date : date
        La date de fin du tournoi
    number_rounds : PositiveInt
        Le nombre de rounds du tournoi
    rounds : List[Round]
        La liste des rounds du toutnoi
    players : List[PlayerId]
        La liste des joueurs du tournoi
    time_control : TimeControl
        Le type de contrôle du temps du tournoi
    description : str
        Les remarques générales du directeur du tournoi
    """
    id: PositiveInt
    name: str
    location: str
    start_date: date = date.today()
    end_date: date = None
    number_rounds: PositiveInt = 4
    rounds: List[Round] = []
    players: List[PlayerId] = []
    time_control: TimeControl
    description: str

    @property
    def is_over(self):
        """
        Utilisation du décorateur @property pour accéder en tant que propriété à l'état d'un tournoi.
        La méthode is_over permet de savoir si un tournoi est terminé en vérifiant si la date de fin est définie.

        Retour
        ------
        Retourne True si la date de fin du tournoi n'est pas None
        sinon retourne False.
        """
        return self.end_date is not None

    @property
    def played_matches(self) -> List[Match]:
        """
        Utilisation du décorateur @property pour accéder en tant que propriété à liste
        des matchs du tournoi déjà joués.
        La méthode played_matches boucle sur chaque match de chaque round du tournoi
        puis vérifie si le match à déjà été joué, si c'est le cas le match est ajouté à la liste played_matches.

        Retour
        ------
        Retourne la liste des matchs du tournoi déjà joués.
        """
        played_matches = []
        for rnd in self.rounds:
            for match in rnd.matches:
                if match.played:
                    played_matches.append(match)
        return played_matches

    @property
    def matches(self) -> List[Match]:
        """
        Utilisation du décorateur @property pour accéder en tant que propriété à liste
        des matchs du tournoi.
        La méthode matches boucle sur chaque match de chaque round du tournoi.

        Retour
        ------
        Retourne la liste des matchs du tournoi.
        """
        return [(match for match in rnd.matches) for rnd in self.rounds]

    def get_player_score(self, player_id: PlayerId):
        """
        Méthode qui permet d'obtenir le score d'un joueur grâce
        à son id en bouclant sur les matchs du tournoi déjà joués.

        Paramètres
        ----------
        player_id : PlayerId
            Id du joueur

        Retour
        ------
        Retourne le score du joueur dont l'id a été passé en paramètre.
        """
        score = 0.
        for match in self.played_matches:
            if match.id_player1 == player_id:
                score += match.score_player1.value
            elif match.id_player2 == player_id:
                score += match.score_player2.value
        return score

    def generate_first_round(self, rnd):
        """
        Méthode qui permet de générer les matchs du premier round du tournoi.
        Elle trie la liste des joueurs du tournoi en fonction de leur classement
        puis la divise en deux moitiés une supérieure et une inférieure.
        Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur
        de la partie inférieure et ainsi de suite pour toute la liste.
        Chaque match est ajouté au premier round du tournoi.

        Paramètres
        ----------
        rnd : Round
            Premier round du tournoi

        Retour
        ------
        Retourne le premier round du tournoi.
        """
        players = sorted([pm.find_by_id(player_id) for player_id in self.players],
                         key=lambda x: (x.rank, x.last_name, x.first_name))
        half = int(len(players)/2)
        rnd.matches += [Match(id_player1=a.id, id_player2=b.id) for a, b in zip(players[half:], players[:half])]
        return rnd

    def generate_match(self, p1, players):
        """
        Méthode qui permet de générer un match entre deux joueurs du tournoi.
        Si le joueur 1 a déjà joué contre le joueur 2 alors on l'associe au joueur suivant.

        Paramètres
        ----------
        p1 : int
            Id du premier joueur du match
        players : List
            Liste des joueurs du tournoi

        Retour
        ------
            Retourne le match généré.
        """
        for p2 in players:
            match = Match(id_player1=p1.id, id_player2=p2.id)
            if match not in self.matches:
                players.pop(players.index(p2))
                return match
        p2 = players.pop(0)
        match = Match(id_player1=p1.id, id_player2=p2.id)
        return match

    def generate_next_round(self, rnd):
        """
        Méthode qui permet de générer les matchs des autres rounds du tournoi.
        Elle trie la liste des joueurs du tournoi en fonction de leur nombre total de points.
        Si plusieurs joueurs ont le même nombre de points alors ils sont trier en fonction de leur classement.
        Le premier joueur est jumelé avec le deuxième joueur et ainsi de suite pour toute la liste.
        On vérifie que les joueurs n'ont pas déjà joués l'un contre l'autre grâce à la méthode generate_match.
        Chaque match est ajouté au round du tournoi.

        Paramètres
        ----------
        rnd : Round
            Un round du tournoi

        Retour
        ------
            Retourne le round du tournoi.
        """
        players = sorted([pm.find_by_id(player_id) for player_id in self.players], key=lambda x: (
            -self.get_player_score(x.id), x.rank))
        while players:
            p1 = players.pop(0)
            match = self.generate_match(p1, players)
            rnd.matches.append(match)
        return rnd

    def generate_round(self, round_name, number_round):
        """
        Méthode qui permet de générer un round en fonction de son numéro.

        Paramètres
        ----------
        round_name : str
            Le nom du round
        number_round : int
            Le numéro du round

        Retour
        ------
        Retourne la méthode generate_first_round ou la méthode generate_next_round
        en fonction du numéro du round.
        """
        rnd = Round(name=round_name)
        if number_round == 1:
            return self.generate_first_round(rnd)
        else:
            return self.generate_next_round(rnd)

    @validator("location", "name")
    def check_len_name(cls, value):
        """
        Utilisation du décorateur @validator pour définir la méthode check_len_name.
        Méthode de validation des champs location et name.
        Vérifie si la longueur du nom entré par l'utilisateur est inférieure à 35 caractères.

        Paramètres
        ----------
        cls : UserModel classe
            La classe Tournament
        value : la valeur du champ à valider
            Les champs location et name

        Retour
        ------
        Retourne la valeur analysée ou lève une ValueError.
        """
        if len(value) > 35:
            raise ValueError("Le nom ne doit pas dépasser 25 caractères.")
        return value

    @validator("players")
    def check_nb_players(cls, value):
        """
        Utilisation du décorateur @validator pour définir la méthode check_nb_players.
        Méthode de validation du champs players.
        Vérifie si le nombre de joueurs entré par l'utilisateur est pair et supérieur ou égal à 2.

        Paramètres
        ----------
        cls : UserModel classe
            La classe Tournament
        value : la valeur du champ à valider
            Le champs players

        Retour
        ------
        Retourne la valeur analysée ou lève une ValueError.
        """
        if len(value) < 2 or len(value) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair et supérieur ou égal à 2.")
        return value

    @validator("players")
    def check_players(cls, value):
        """
        Utilisation du décorateur @validator pour définir la méthode check_players.
        Méthode de validation du champs players.
        Vérifie si l'id du joueur entré par l'utilisateur existe et
        si le joueur n'est pas déjà inscrit dans le tournoi.

        Paramètres
        ----------
        cls : UserModel classe
            La classe Tournament
        value : la valeur du champ à valider
            Le champs players

        Retour
        ------
        Retourne la valeur analysée ou lève une ValueError.
        """
        count = Counter(value)
        for c in dict(count):
            if count[c] > 1:
                raise ValueError("Un joueur ne peut pas s'inscrire plusieurs fois dans un tournoi.")
        for player_id in value:
            pm.find_by_id(player_id)
        return value

    @validator("description")
    def check_description(cls, value):
        """
        Utilisation du décorateur @validator pour définir la méthode check_description.
        Méthode de validation du champs description.
        Vérifie si la longueur de la description entrée par l'utilisateur est inférieure à 150 caractères.

        Paramètres
        ----------
        cls : UserModel classe
            La classe Tournament
        value : la valeur du champ à valider
            Le champs description

        Retour
        ------
        Retourne la valeur analysée ou lève une ValueError.
        """
        if len(value) > 150:
            raise ValueError("La description du tournoi ne doit pas dépasser 150 caractères.")
        return value
