from pipes_filters.filter import Filter


class WordCountFilter(Filter):
    """Conta o número de palavras em uma string."""

    def execute(self, data: str) -> int:
        return len(data.split())