"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, TrimFilter, ReplaceFilter, MaskCPFFilter, RemoveAcentFilter

def main() -> None:
    entrada = "Arquitetura de Software"
    entrada2 = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "
    entrada3 = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "
    entrada4 = "123.456.789-00"
    entrada5 = "Olá, meu nome é João Olíveira e estou indo para São Paulo."

    pipeline = (
        Pipe()
        .add(UppercaseFilter())
        .add(ReverseFilter())
    )
    pipeline2 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("João", "Pedro"))
    )
    pipeline3 = (
        Pipe()
        .add(ReplaceFilter("da", "de"))
        .add(ReplaceFilter("Silva", "Souza"))
        .add(TrimFilter())
    )
    pipeline4 = (
        Pipe()
        .add(MaskCPFFilter())
    )
    pipeline5 = (
        Pipe()
        .add(RemoveAcentFilter())
    )

    saida = pipeline.run(entrada)
    saida2 = pipeline2.run(entrada2)
    saida3 = pipeline3.run(entrada3)
    saida4 = pipeline4.run(entrada4)
    saida5 = pipeline5.run(entrada5)

    print("Pipeline montado :", pipeline)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))
    print("\nPipeline montado :", pipeline2)
    print("Entrada 2        :", repr(entrada2))
    print("Saida 2          :", repr(saida2))
    print("\nPipeline montado :", pipeline3)
    print("Entrada 3        :", repr(entrada3))
    print("Saida 3          :", repr(saida3))
    print("\nPipeline montado :", pipeline4, "(Opcional)")
    print("Entrada 4        :", repr(entrada4))
    print("Saida 4          :", repr(saida4))
    print("\nPipeline montado :", pipeline5, "(Opcional)")
    print("Entrada 5        :", repr(entrada5))
    print("Saida 5          :", repr(saida5))



if __name__ == "__main__":
    main()
