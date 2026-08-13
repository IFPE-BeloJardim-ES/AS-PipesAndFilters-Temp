"""Filtro que remove espaços em branco extras de uma string.

Existe para que o pipeline tenha mais de uma etapa e o papel do Pipe
fique visivel.

Utilizei da forma " ".join(data.slit())
Onde o Split separa as palavras de uma string e o Join junta as palavras separadas por um espaço.
Deixando assim bem amis simples de entender e mais legível.
"""
from pipes_filters.filter import Filter

class TrimFilter(Filter):
    def execute(self, data):
        return " ".join(data.split())