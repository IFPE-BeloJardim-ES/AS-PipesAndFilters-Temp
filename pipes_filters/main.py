"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, ReplaceFilter, TrimFilter


def main() -> None:
    entrada = " Arquitetura de Software "
    texto = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    pipeline = (
        Pipe()
        .add(UppercaseFilter())
        .add(ReverseFilter())
        .add(ReplaceFilter("Arquitetura", "Engenharia"))
        .add(TrimFilter())
    )

    pipeline_1 = (
        Pipe()
        .add(ReplaceFilter("João", "Randson"))
        .add(TrimFilter())
    )

    pipeline_2 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("João", "Randson"))
    )

    saida = pipeline.run(entrada)
    saida_1 = pipeline_1.run(texto)
    saida_2 = pipeline_2.run(texto)

    print("Pipeline montado :", pipeline)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))

    print("Pipeline 1 montado :", pipeline_1)
    print("Entrada 1         :", repr(texto))
    print("Saida 1          :", repr(saida_1))

    print("Pipeline 2 montado :", pipeline_2)
    print("Entrada 2         :", repr(texto))
    print("Saida 2          :", repr(saida_2))


if __name__ == "__main__":
    main()
