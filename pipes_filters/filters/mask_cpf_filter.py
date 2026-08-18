import re
from pipes_filters.filter import Filter


class MaskCpfFilter(Filter):
    """Encontra CPFs no texto (formatados ou apenas digitos) e substitui por ***.***.***-**."""

    def execute(self, data: str) -> str:
        # Regex para CPFs formatados (000.000.000-00) ou nao formatados (00000000000)
        cpf_pattern = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b"
        return re.sub(cpf_pattern, "***.***.***-**", data)