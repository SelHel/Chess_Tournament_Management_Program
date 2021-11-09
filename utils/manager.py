import json
from pydantic.types import PositiveInt
from tinydb import TinyDB
from tinydb.table import Document


class Manager:
    """Permet de gérer une collection d'objets."""
    def __init__(self, item_type: type):
        """
        Construit tous les attributs nécessaires pour l'objet Manager.

        Paramètres
        ----------
        item_type: type
            Le type de l'objet à gérer
        """
        self.items = {}
        self.item_type = item_type
        self.max_id = 0
        db = TinyDB("db.json", sort_keys=True, indent=4)
        self.table = db.table(self.item_type.__name__.lower() + "s")
        for item_data in self.table:
            self.create_item(**item_data)

    def save_item(self, id: PositiveInt):
        """
        Méthode permettant de sauvegarder un objet dans la base de données.

        Paramètres
        ----------
        id : PositiveInt
            L'id de l'objet à sauvegarder
        """
        item = self.find_by_id(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))

    def create_item(self, *args, **kwargs):
        """
        Méthode permettant la création puis la sauvegarde d'un objet dans la base de données.

        Paramètres
        ----------
        *args : arguments sans mots-clés
        **kwargs : arguments avec mots-clés

        Retour
        ------
        Retourne l'objet nouvellement créé.
        """
        item = self.item_type(*args, **kwargs)
        self.items[item.id] = item
        self.max_id = max(item.id, self.max_id)
        self.save_item(item.id)
        return item

    def find_all(self):
        """
        Méthode permettant de trouver tous les objets de la classe.

        Retour
        ------
        Retourne la liste de tous les objets de la classe item_type.
        """
        return list(self.items.values())

    def find_by_id(self, id: any) -> any:
        """
        Méthode permettant de trouver un objet grâce à son id.

        Paramètres
        ----------
        id : any
            L'id de l'objet

        Retour
        ------
        Retourne l'objet correspondant à l'id passé en paramètre.
        """
        return self.items[id]
