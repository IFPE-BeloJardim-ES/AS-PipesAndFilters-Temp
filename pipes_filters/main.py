"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, ReplaceFilter, TrimFilter


def main() -> None:
    entrada = "Arquitetura de Software"

    pipeline = (
        Pipe()
        .add(ReplaceFilter("Arquitetura", "Engenharia"))
        .add(UppercaseFilter())
        .add(ReverseFilter())
    )

    saida = pipeline.run(entrada)

    print("Pipeline montado :", pipeline)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))

    entrada2 = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "
    pipeline2 = (
        Pipe()
        .add(ReplaceFilter("João", "Maria"))
        .add(TrimFilter())
    )

    saida2 = pipeline2.run(entrada2)
    print("Pipeline montado :", pipeline2)
    print("Entrada          :", repr(entrada2))
    print("Saida            :", repr(saida2))


if __name__ == "__main__":
    main()
