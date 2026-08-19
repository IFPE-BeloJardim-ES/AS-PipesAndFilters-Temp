# 3° - filtro usado para remover espaços

from pipes_filters.filter import Filter


class TrimFilter(Filter):
#     Remove os espaços das pontas e transforma sequências de espaços em um espaço só.

    def execute(self, data: str) -> str:
        new_data = " ".join(data.split())

        return new_data
