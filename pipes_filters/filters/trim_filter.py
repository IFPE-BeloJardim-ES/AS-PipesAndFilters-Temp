"""Filtro que normaliza os espacos do texto."""

from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove espacos das pontas e espacos repetidos no meio."""

    def execute(self, data):
        # O split sem argumento separa por qualquer espaco e o join junta com um so
        return " ".join(data.split())
