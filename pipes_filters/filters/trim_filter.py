from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove os espaços das pontas e transforma sequências de espaços em um espaço só."""
    def execute(self, data: str) -> str:
        return " ".join(data.split())