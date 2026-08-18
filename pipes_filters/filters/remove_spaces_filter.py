from pipes_filters.filter import Filter

class RemoveSpacesFilter(Filter):
    """
    Filtro de exemplo: Remove todos os espaços em branco da string recebida.
    """
    def execute(self, data: str) -> str:
        # Substitua a lógica abaixo pela regra exata do seu ATIVIDADE.md
        return data.replace(" ", "")
