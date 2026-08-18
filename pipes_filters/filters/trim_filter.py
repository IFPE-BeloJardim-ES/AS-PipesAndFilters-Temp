from pipes_filters.filter import Filter

class TrimFilter(Filter):
    """Remove os espaços das pontas e transforma sequências de espaços em um espaço só."""

    def execute(self, data: str) -> str:
        # verifica se é uma string antes de tentar processar
        if not isinstance(data, str):
            return data
        return ' '.join(data.split())
