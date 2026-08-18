from pipes_filters.filter import Filter
import re

class MaskCpfFilter(Filter):
    """Encontra CPFs no texto (formatados ou não) e substitui por ***.***.***-**"""

    def execute(self, data: str) -> str:
        return re.sub(r'(\d{3})\.?(\d{3})\.?(\d{3})-?(\d{2})', r'***.***.***-**', data)
