"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, TrimFilter, ReplaceFilter


def main() -> None:
    entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    pipeline1 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("Silva", "Souza"))
    )
    saida1 = pipeline1.run(entrada)

    pipeline2 = (
        Pipe()
        .add(ReplaceFilter("Silva", "Souza"))
        .add(TrimFilter())
    )
    saida2 = pipeline2.run(entrada)

    print("Pipeline 1 montado :", pipeline1)
    print("Entrada            :", repr(entrada))
    print("Saida 1            :", repr(saida1))
    print()
    print("Pipeline 2 montado :", pipeline2)
    print("Entrada            :", repr(entrada))
    print("Saida 2            :", repr(saida2))


if __name__ == "__main__":
    main()