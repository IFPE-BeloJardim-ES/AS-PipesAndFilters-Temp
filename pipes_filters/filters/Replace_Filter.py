from pipes_filters.filter import Filter

class ReplaceFilter(Filter):
    """Substitui todas as ocorrencias de uma substring por outra."""
    def __init__(self, alvo: str, substituto: str) -> None:
        self.alvo = alvo
        self.substituto = substituto
    def execute(self, data: str) -> str:
        return data.replace(self.alvo, self.substituto)