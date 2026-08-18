"""Filtro: remove espaços extras da entrada."""

from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove espaços das pontas e reduz espaços internos a um só."""

    def execute(self, data: str) -> str:
        return " ".join(data.split())