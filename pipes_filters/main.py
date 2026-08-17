"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import TrimFilter, ReplaceFilter, WordCountFilter


def main() -> None:
    entrada = "  O   cliente João  da  Silva,   CPF 123.456.789-00   "

    pipeline_1 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("cliente", "usuário"))
        .add(WordCountFilter())
    )

    pipeline_2 = (
        Pipe()
        .add(ReplaceFilter("cliente", "usuário"))
        .add(TrimFilter())
        .add(WordCountFilter())
    )

    saida_1 = pipeline_1.run(entrada)
    saida_2 = pipeline_2.run(entrada)

    print("Pipeline 1       :", pipeline_1)
    print("Entrada 1        :", repr(entrada))
    print("Saida 1          :", repr(saida_1))
    print()
    print("Pipeline 2       :", pipeline_2)
    print("Entrada 2        :", repr(entrada))
    print("Saida 2          :", repr(saida_2))


if __name__ == "__main__":
    main()
