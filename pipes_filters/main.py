"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import TrimFilter, ReplaceFilter, MaskCpfFilter


def main():
    texto_entrada = "   O   cliente João  da   Silva,  CPF 123.456.789-00  "

    # Pipeline 1: TrimFilter -> ReplaceFilter
    pipeline1 = Pipe()
    pipeline1.add(TrimFilter())
    pipeline1.add(ReplaceFilter("João", "Maria"))
    pipeline1.add(MaskCpfFilter())

    # Pipeline 2: ReplaceFilter -> TrimFilter
    pipeline2 = Pipe()
    pipeline2.add(ReplaceFilter("João", "Maria"))
    pipeline2.add(TrimFilter())
    pipeline2.add(MaskCpfFilter())

    print("=== PIPELINE 1 (Trim -> Replace) ===")
    print(f"Entrada: '{texto_entrada}'")
    print(f"Saída  : '{pipeline1.run(texto_entrada)}'\n")

    print("=== PIPELINE 2 (Replace -> Trim) ===")
    print(f"Entrada: '{texto_entrada}'")
    print(f"Saída  : '{pipeline2.run(texto_entrada)}'")


if __name__ == "__main__":
    main()