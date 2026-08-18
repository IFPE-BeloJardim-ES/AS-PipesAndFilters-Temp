"""Filtro que remove espaços das pontas e normaliza espaços múltiplos."""

from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove espaços das pontas e transforma sequências de espaços em um espaço só."""

    def execute(self, data: str) -> str:
        # Remove espaços das pontas
        data = data.strip()
        # Substitui múltiplos espaços por um único espaço
        return " ".join(data.split())
