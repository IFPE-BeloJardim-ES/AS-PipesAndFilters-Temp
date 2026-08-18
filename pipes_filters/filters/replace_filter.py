"""Filtro: substitui uma palavra por outra."""

from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
    """Troca todas as ocorrências de uma palavra por outra.

    As palavras são definidas na criação do filtro, não no execute.
    """

    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new

    def execute(self, data: str) -> str:
        return data.replace(self.old, self.new)