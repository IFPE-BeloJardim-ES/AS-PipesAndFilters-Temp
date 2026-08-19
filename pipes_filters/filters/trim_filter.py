from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove espaços das pontas e transforma sequências de espaços em um só."""

    def execute(self, data: str) -> str:
        # split() sem argumentos separa a string por qualquer quantidade de whitespace
        # e join(' ') junta com exatamente um espaço.
        # Isso também remove os espaços das pontas.
        return ' '.join(data.split())
