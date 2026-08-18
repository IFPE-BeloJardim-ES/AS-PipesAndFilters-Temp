"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import TrimFilter, ReplaceFilter


def main():
    texto = "   O   cliente Eng  Pedro da  Silva,  CPF 123.456.789-00  "

    pipeline1 = Pipe()
    pipeline1.add(TrimFilter())
    pipeline1.add(ReplaceFilter("Silva", "Santos"))
    pipeline1.add(ReplaceFilter("da", "dos"))

    resultado1 = pipeline1.run(texto)

    pipeline2 = Pipe()
    pipeline2.add(ReplaceFilter("Pedro", "Gustavo"))
    pipeline2.add(TrimFilter())

    resultado2 = pipeline2.run(texto)

    print("Texto original:")
    print(f'"{texto}"')
    print()
    print("Pipeline 1 (TrimFilter -> ReplaceFilter):")
    print(f'"{resultado1}"')
    print()
    print("Pipeline 2 (ReplaceFilter -> TrimFilter):")
    print(f'"{resultado2}"')


if __name__ == "__main__":
    main()