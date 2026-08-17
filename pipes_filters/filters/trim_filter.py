import re
from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove espaços das pontas e reduz múltiplos espaços internos a um só."""

    def execute(self, data: str) -> str:
        # \s+ pega um ou mais espaços em sequência e substitui por um único espaço
        return re.sub(r"\s+", " ", data).strip()