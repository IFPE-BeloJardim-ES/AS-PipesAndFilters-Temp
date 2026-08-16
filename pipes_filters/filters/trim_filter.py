from pipes_filters.filter import Filter


class TrimFilter(Filter):
    """Remove os espaços das pontas e transforma sequências de espaços em um espaço só."""

    def execute(self, data):
        # verifica se é uma string antes de tentar processar
        if isinstance(data, str):
            return " ".join(data.split())
        
        # se não for retorna o dado original sem alterar
        return data