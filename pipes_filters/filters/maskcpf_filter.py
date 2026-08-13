"""
Filtro para mascarar o CPF.
Utilizei da biblioteca Regex para fazer a substituição do CPF por ***.***.***-**.
idependente se estiver formatado ou não.
"""

from pipes_filters.filter import Filter
import re

class MaskCPFFilter(Filter):
    def execute(self, data):
        # responsavel por trocar o CPF Formatado ou não 12345678900 or 123.456.789-00
        pattern = r"\d{3}\.??\d{3}\.??\d{3}-?\d{2}"
        return re.sub(pattern, "***.***.***-**", data)