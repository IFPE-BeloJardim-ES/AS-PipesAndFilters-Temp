"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe
from pipes_filters.filters import UppercaseFilter, ReverseFilter, TrimFilter, ReplaceFilter


def main() -> None:
    entrada_exemplo = "Arquitetura de Software"
    entrada_1 = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    pipeline_exemplo = (
        Pipe()
        .add(UppercaseFilter())
        .add(ReverseFilter())
        .add(TrimFilter())
        .add(ReplaceFilter("Software", "Sistemas")) 
        #Com essa pipeline o ReplaceFilter não é executado porque 'Software'
        #virou 'ERAWTFOS' 
    )
    
    pipeline_1 = (
        Pipe()
        .add(TrimFilter())
        .add(ReplaceFilter("João", "Severino"))
    )
    
    pipeline_2 = (
        Pipe()
        .add(ReplaceFilter("João", "Severino"))
        .add(TrimFilter())
    )

    saida_exemplo = pipeline_exemplo.run(entrada_exemplo)
    saida_1 = pipeline_1.run(entrada_1)
    saida_2 = pipeline_2.run(entrada_1)

    print("Pipeline montado :", pipeline_exemplo)
    print("Entrada          :", repr(entrada_exemplo))
    print("Saida            :", repr(saida_exemplo))
    print("<-------------------------------------------------------------------------->")
    print("Pipeline_1 montado :", pipeline_1)
    print("Entrada          :", repr(entrada_1))
    print("Saida            :", repr(saida_1))
    print("<-------------------------------------------------------------------------->")
    print("Pipeline_2 montado :", pipeline_2)
    print("Entrada          :", repr(entrada_1))
    print("Saida            :", repr(saida_2))

if __name__ == "__main__":
    main()


    