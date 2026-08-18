"""Filtro que substitui uma palavra por outra."""

from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
    """Substitui uma palavra por outra no texto."""

    def __init__(self, old_word: str, new_word: str):
        """Inicializa o filtro com a palavra a ser substituída e a nova palavra.
        
        Args:
            old_word: Palavra a ser substituída
            new_word: Palavra que vai substituir
        """
        self.old_word = old_word
        self.new_word = new_word

    def execute(self, data: str) -> str:
        return data.replace(self.old_word, self.new_word)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}('{self.old_word}' -> '{self.new_word}')>"
