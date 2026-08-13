"""Filtro que troca uma palavra por outra em uma string.

Existe para que o pipeline tenha mais de uma etapa e o papel do Pipe
fique visivel.

Utilizei o proprio replace do python para fazer a troca
Onde por meio da def__init__ o filtro recebe as palavras e as armazenam dentro de suas proprias variaveis.
"""
from pipes_filters.filter import Filter

class ReplaceFilter(Filter):
    def __init__(self, palavra_antiga, palavra_nova):
        self.palavra_antiga = palavra_antiga
        self.palavra_nova = palavra_nova
    def execute(self, data):
        return data.replace(self.palavra_antiga, self.palavra_nova)
    

