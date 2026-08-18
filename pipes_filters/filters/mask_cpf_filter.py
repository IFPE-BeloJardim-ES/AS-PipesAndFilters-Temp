import re
from pipes_filters.filter import Filter

class MaskCpfFilter(Filter):
    """Encontra CPFs no texto e substitui por ***.***.***-**."""

    def execute(self, data: str) -> str:
        if not isinstance(data, str):
            return data
        
        # Regex captura CPFs formatados (123.456.789-00) ou apenas números (12345678900)
        padrao_cpf = r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b'
        return re.sub(padrao_cpf, '***.***.***-**', data)
