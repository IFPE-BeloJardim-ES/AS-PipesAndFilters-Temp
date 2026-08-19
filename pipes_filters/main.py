"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, TrimFilter, ReplaceFilter


def main() -> None:
    entrada = "Arquitetura de Software"

    pipeline = (
        Pipe()
        .add(UppercaseFilter())
        .add(ReverseFilter())
    )

    saida = pipeline.run(entrada)

    print("Pipeline montado :", pipeline)
    print("Entrada          :", repr(entrada))
    print("Saída            :", repr(saida))

    #Pipeline 2
    entrada2 = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    pipeline2 = (
            Pipe()
            .add(TrimFilter())
            .add(ReplaceFilter('Software', 'Sistemas'))
        )
    
    saida2 = pipeline2.run(entrada2)

    print("\nPipeline montado 2 :", pipeline2)
    print("Entrada            :", repr(entrada2))
    print("Saída              :", repr(saida2))

    #Pipeline 3
    entrada3 = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    pipeline3 = (
            Pipe()
            .add(ReplaceFilter('Software', 'Sistemas'))
            .add(TrimFilter())
        )
    
    saida3 = pipeline3.run(entrada3)

    print("\nPipeline montado 3 :", pipeline3)
    print("Entrada            :", repr(entrada3))
    print("Saída              :", repr(saida3))


if __name__ == "__main__":
    main()
