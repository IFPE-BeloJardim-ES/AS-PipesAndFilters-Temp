from pipes_filters.filter import Filter


class TrimFilter(Filter):
    def execute(self, data: str) -> str:
        return " ".join(data.split())