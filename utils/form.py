from typing import List, Tuple, Any
from utils.enum_menu import EnumMenu
from utils.view import View


class Form(View):
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        self.fields = fields
        super().__init__(title)

    def display(self):
        data = {}
        super().display()
        for field, description, field_type in self.fields:
            while True:
                try:
                    if isinstance(field_type(), EnumMenu):
                        data[field] = field_type().display()
                        break
                except TypeError:
                    pass
                try:
                    data[field] = field_type(input(description + " : "))
                    break
                except ValueError:
                    pass
        return data
