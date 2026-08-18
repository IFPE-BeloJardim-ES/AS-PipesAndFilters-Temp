from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Retira os espaços em branco no inicio e fim da string"""
    def execute(self, data: str) -> str:
        return data.strip()