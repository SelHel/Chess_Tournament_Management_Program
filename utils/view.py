import os


class View:
    """Classe représentant une vue."""
    def __init__(self, title: str, content: str = "", blocking: bool = False):
        """
        Construit tous les attributs nécessaires à l'objet View.
        La vue présente les informations du modèle à l’utilisateur.
        Elle sert d’interface visuelle pour l’utilisateur.

        Paramètres
        ----------
        title : str
            Titre de la vue
        content : str, facultatif
            Contenu de la vue
        blocking: bool
            blocage de la vue
        """
        self.title = title
        self.content = content
        self.blocking = blocking

    def display(self):
        """
        Méthode permettant d'afficher une vue.
        Affiche le titre de la vue.
        Affiche le contenu de la vue si il n'y a pas de blocage.

        Retour
        ------
        Retourne le contenu si il y a un blocage.
        """
        os.system("clear")
        print(self.title)
        print("-" * len(self.title))
        if self.content:
            if not self.blocking:
                print(self.content)
            else:
                return input(self.content + "\n: ")
