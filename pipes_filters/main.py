"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, TrimFilter, ReplaceFilter


def main() -> None:
    # Texto de entrada para os dois pipelines
    entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    # Pipeline 1: TrimFilter primeiro, depois ReplaceFilter
    pipeline1 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("João", "Maria"))
    )

    saida1 = pipeline1.run(entrada)

    print("=" * 70)
    print("PIPELINE 1: TrimFilter → ReplaceFilter")
    print("=" * 70)
    print("Pipeline montado :", pipeline1)
    print("Entrada          :", repr(entrada))
    print("Saída            :", repr(saida1))

    # Pipeline 2: ReplaceFilter primeiro, depois TrimFilter (ordem trocada)
    pipeline2 = (
        Pipe()
        .add(ReplaceFilter("João", "Maria"))
        .add(TrimFilter())
    )

    saida2 = pipeline2.run(entrada)

    print("\n" + "=" * 70)
    print("PIPELINE 2: ReplaceFilter → TrimFilter")
    print("=" * 70)
    print("Pipeline montado :", pipeline2)
    print("Entrada          :", repr(entrada))
    print("Saída            :", repr(saida2))

    print("\n" + "=" * 70)
    print("COMPARAÇÃO")
    print("=" * 70)
    print(f"Os resultados são iguais? {saida1 == saida2}")
    if saida1 == saida2:
        print("Resultado: Ambos os pipelines produziram a mesma saída")
    else:
        print("Resultado: Os pipelines produziram saídas diferentes")


if __name__ == "__main__":
    main()
