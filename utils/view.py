import os


class View:
    """Classe représentant une vue."""
    def __init__(self, title: str, content: str = "", with_input: bool = False):
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
        with_input: bool
            Paramètre pour indiquer si c'est un print(affichage classique) ou
            si c'est un input(affichage puis attente d'une action utilisateur)
        """
        self.title = title
        self.content = content
        self.with_input = with_input

    def display(self):
        """
        Méthode permettant d'afficher une vue.
        Affiche le titre et le contenu de la vue.

        Retour
        ------
        Print le contenu ou affiche le contenu suivi d'un input.
        """
        os.system("clear")
        print(self.title)
        print("-" * len(self.title))
        if self.content:
            if not self.with_input:
                print(self.content)
            else:
                return input(self.content + "\n: ")
