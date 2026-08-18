"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
# Adicione o seu novo filtro na importação abaixo:
from pipes_filters.filters import UppercaseFilter, ReverseFilter, RemoveSpacesFilter


def main() -> None:
    entrada = "Arquitetura de Software"

    # Adicione o seu filtro chamando mais um .add() na ordem desejada
    pipeline = (
        Pipe()
        .add(UppercaseFilter())
        .add(RemoveSpacesFilter())  # <-- Seu novo filtro plugado aqui
        .add(ReverseFilter())
    )

    saida = pipeline.run(entrada)

    print("Pipeline montado :", pipeline)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))


if __name__ == "__main__":
    main()
