from pipes_filters.filter import Filter


class WordCounterFilter(Filter):
    """Devolve a quantidade de palavras."""

    def execute(self, data: str) -> str:
        return str(len(data.split()))
