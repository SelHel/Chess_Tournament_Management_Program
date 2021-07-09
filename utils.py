import json
from typing import Callable


class Manager:
    """Gérer une collection d'objets"""
    def __init__(self, item_type: type, id_finder: Callable[[any], any]):
        self.items = {}
        self.item_type = item_type
        self.id_finder = id_finder
    
    def load_from_json(self, path: str):
        with open(path) as file:
            for item_data in json.load(file):
                self.create_item(**item_data)
    
    def create_item(self, *args, **kwargs):
        item = self.item_type(*args, **kwargs)
        self.items[self.id_finder(item)] = item
        return item
    
    def find_all(self):
        return list(self.items.values())
    
    def find_by_id(self, id: any) -> any:
        return self.items[id]

