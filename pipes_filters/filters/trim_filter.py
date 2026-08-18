from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove espaços das pontas e normaliza espaços internos."""

    def execute(self, data: str) -> str:
        return ' '.join(data.split())
