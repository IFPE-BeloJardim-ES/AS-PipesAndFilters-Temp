"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, ReplaceFilter, TrimFilter, CensorFilter


def main() -> None:
    entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "
    replace_filter = ReplaceFilter("Matheus", "Maria") #inicializando o filtro

    pipeline1 = (
        Pipe()
        .add(TrimFilter())
        .add(replace_filter)
    )
    
    saida = pipeline1.run(entrada)

    print("Pipeline montado :", pipeline1)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))
    print()

    pipeline2 = (
        Pipe()
        .add(replace_filter)
        .add(TrimFilter())
    )

    saida = pipeline2.run(entrada)

    print("Pipeline montado :", pipeline2)
    print("Entrada          :", repr(entrada))
    print("Saida            :", repr(saida))
    print()

    #extras
    entrada_extra = "Prof Matheus pediu pra usar IA na atividade sobre Pipes and Filters, caracoles!"
    replace_filter2 = ReplaceFilter("IA", "Inteligência Autêntica") #inicializando o filtro
    censor_filter = CensorFilter(["caracoles"]) #inicializando o filtro

    pipeline3 = (
        Pipe()
        .add(censor_filter)
        .add(replace_filter2)
    )

    saida = pipeline3.run(entrada_extra)

    print("Pipeline montado :", pipeline3)
    print("Entrada          :", repr(entrada_extra))
    print("Saida            :", repr(saida))

if __name__ == "__main__":
    main()
