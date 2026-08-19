"""Ponto de entrada: monta o pipeline e executa.

Este e o UNICO arquivo que muda quando um filtro novo entra no sistema.
Nem o Pipe nem os filtros existentes precisam ser tocados -- essa e a
propriedade que a arquitetura Pipes and Filters entrega.
"""

from pipes_filters.pipe import Pipe

from pipes_filters.filters import UppercaseFilter, ReverseFilter, trim_filter,Replace_Filter


def main() -> None:
    entrada = "   Arquitetura de Software   "
    Segunda_entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "
    Terceira_entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "
    pipeline = (
        Pipe()
        .add(UppercaseFilter())
        .add(ReverseFilter())
        .add(trim_filter.TrimFilter()) 
        .add(Replace_Filter.ReplaceFilter("Software", "Sistemas"))
    )
    
    Pipeline_dois = (
        Pipe()
        .add(trim_filter.TrimFilter()) 
        .add(Replace_Filter.ReplaceFilter("Cliente", "Funcionario"))
    )

    
    Pipeline_tres = (
        Pipe()
        .add(Replace_Filter.ReplaceFilter("Cliente", "Funcionario"))
        .add(trim_filter.TrimFilter()) 
        
    )
    saida = pipeline.run(entrada)
    segunda_saida = Pipeline_dois.run(Segunda_entrada)
    Terceira_saida = Pipeline_tres.run(Terceira_entrada)
    
    print("Pipeline montado :", Pipeline_dois)
    print("Entrada          :", repr(Segunda_entrada))
    print("Saida            :", repr(segunda_saida))

    print("Pipeline montado :", Pipeline_tres)
    print("Entrada          :", repr(Terceira_entrada))
    print("Saida            :", repr(Terceira_saida))
    
    
    

if __name__ == "__main__":
    main()