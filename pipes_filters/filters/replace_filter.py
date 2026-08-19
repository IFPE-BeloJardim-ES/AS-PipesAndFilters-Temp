# 4° filtro - usado para substituir palavras

from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
#    Substitui uma palavra por outra

    def __init__(self, old_word: str, new_word: str):
        # Recebe os parâmetros de substituição na criação do filtro
        self._old_word = old_word
        self._new_word = new_word

    def execute(self, data: str) -> str:
        # Utiliza o replace() das strings usando os parâmetros salvos no construtor
        return data.replace(self._old_word, self._new_word)