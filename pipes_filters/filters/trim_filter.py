from pipes_filters.filter import Filter
import re

class TrimFilter(Filter):

    def execute(self, data: str) -> str:
        data = data.strip()
        data = re.sub(r'\s+', ' ', data)
        return data

