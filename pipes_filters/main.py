"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import TrimFilter, ReplaceFilter


def main() -> None:
    entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    pipeline1 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("Software", "Sistemas"))
    )

    pipeline2 = (
        Pipe()
        .add(ReplaceFilter("Software", "Sistemas"))
        .add(TrimFilter())
    )

    saida1 = pipeline1.run(entrada)
    saida2 = pipeline2.run(entrada)

    print("--- Pipeline 1 ---")
    print("Montado :", pipeline1)
    print("Entrada :", repr(entrada))
    print("Saida   :", repr(saida1))
    print("\n--- Pipeline 2 ---")
    print("Montado :", pipeline2)
    print("Entrada :", repr(entrada))
    print("Saida   :", repr(saida2))


if __name__ == "__main__":
    main()
