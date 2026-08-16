from pipes_filters.filter import Filter


class CensorFilter(Filter):
    """Recebe uma lista de palavras proibidas na criação e troca cada uma por asteriscos."""

    def __init__(self, forbidden_words: list[str]):
        self._forbidden_words = forbidden_words

    def execute(self, data):
        for word in self._forbidden_words:
            data = data.replace(word, "*" * len(word))
        return data