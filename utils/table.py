from typing import List, Any
from utils.view import View


class Table(View):
    def __init__(self, title: str, items: List[Any]):
        super().__init__(title, content="  "+self._format_header()+"\n"+"─"*110 + "\n" + "\n".join([
                            "  " + self._format_item(item) + "\n"
                            + "─"*110 for item in items]) + "\n", blocking=True)

    def _format_header():
        pass

    def _format_item(item: Any):
        pass
