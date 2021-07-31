
from typing import List, Tuple, Any
from utils.view import View


class Form(View):
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        self.fields = fields
        super().__init__(title)

    def display(self):
        data = {}
        super().display()
        for field, description, field_type in self.fields:
            data[field] = field_type(input(description + " ? "))
        return data


form = Form("Formulaire", [("last_name", "Nom", str), ("age", "Age", int)])

print(form.display())