"""Filtro que substitui uma palavra por outra."""

from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
    """Troca todas as ocorrencias de uma palavra por outra."""

    def __init__(self, antiga, nova):
        self._antiga = antiga
        self._nova = nova

    def execute(self, data):
        return data.replace(self._antiga, self._nova)
