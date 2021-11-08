from typing import (Any, Callable, List, Tuple)
from .menu import Menu


class Table(Menu):
    """Classe représentant une table."""
    def __init__(
        self,
        title: str,
        items: List[Any],
        cols: List[Tuple[str, int, Callable[[Any], Any]]],
        choices: List[Tuple[str, str]] = []
    ):
        """
        Construit tous les attributs nécessaires à l'objet Table.

        Paramètres
        ----------
        title : str
            Titre de la table
        items : List[Any]
            Liste des éléments de la table
        cols : List[Tuple[str, int, Callable[[Any], Any]]]
            Liste des colonnes de la table
        choices: List[Tuple[str, str]]
            Liste des choix de la table 
        """
        self.cols = cols
        super().__init__(title, choices, self._gen_content(items))

    def _gen_content(self, items: List[Any]):
        line_length = self._line_length()
        return "  " + self._format_header() + "\n" + \
            "─" * line_length + "\n" + "\n".join(
                ["  " + self._format_line(item) + "\n" + "─" * line_length for item in items])

    def _line_length(self):
        line_length = 0
        for _, length, _ in self.cols:
            line_length += length
        return line_length + 4

    def _format_header(self):
        header = ""
        for label, length, _ in self.cols:
            header += label.center(length)
        return header

    def _format_line(self, item: Any):
        line = ""
        for _, length, func in self.cols:
            line += str(func(item)).center(length)
        return line
