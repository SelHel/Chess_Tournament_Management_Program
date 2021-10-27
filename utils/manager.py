import json
from pydantic.types import PositiveInt
from tinydb import TinyDB
from tinydb.table import Document


class Manager:
    """Permet de gérer une collection d'objets"""
    def __init__(self, item_type: type):
        self.items = {}
        self.item_type = item_type
        self.max_id = 0
        db = TinyDB("db.json", sort_keys=True, indent=4)
        self.table = db.table(self.item_type.__name__.lower() + "s")
        for item_data in self.table:
            self.create_item(**item_data)

    def save_item(self, id: PositiveInt):
        """Permet de sauvegarder un objet."""
        item = self.find_by_id(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))

    def create_item(self, *args, **kwargs):
        """Permet la création d'un objet et fait une sauvegarde du nouvel objet."""
        item = self.item_type(*args, **kwargs)
        self.items[item.id] = item
        self.max_id = max(item.id, self.max_id)
        self.save_item(item.id)
        return item

    def find_all(self):
        """Retourne la liste de tous les objets."""
        return list(self.items.values())

    def find_by_id(self, id: any) -> any:
        """Retourne l'objet correspondant à l'id passé en paramètre."""
        return self.items[id]
