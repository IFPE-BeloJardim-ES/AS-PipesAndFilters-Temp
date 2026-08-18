"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, TrimFilter, ReplaceFilter


def main() -> None:
    entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    # pipeline = (
    #     Pipe()
    #     .add(UppercaseFilter())
    #     .add(ReverseFilter())
    # )

    pipeline1 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("João", "Xavier"))
    )

    pipeline2 = (
        Pipe()
        .add(ReplaceFilter("João", "Xavier"))
        .add(TrimFilter())
    )

    saida1 = pipeline1.run(entrada)
    saida2 = pipeline2.run(entrada)

    print(
        f"""
        Pipeline 1 montado : {pipeline1}
        Entrada 1          : {repr(entrada)}
        Saida 1            : {repr(saida1)}

        Pipeline 2 montado : {pipeline2}
        Entrada 2          : {repr(entrada)}
        Saida 2            : {repr(saida2)}

        """)


if __name__ == "__main__":
    main()
