from pipes_filters.pipe import Pipe
from pipes_filters.filters import TrimFilter, ReplaceFilter


def main():
    texto_entrada = "   O   cliente João  da  Silva,  CPF 123.456.789-00  "

    # Pipeline 1: TrimFilter -> ReplaceFilter
    pipeline1 = Pipe().add(TrimFilter()).add(ReplaceFilter("Software", "Sistemas"))
    # AQUI: troque execute por run
    resultado1 = pipeline1.run(texto_entrada)

    print("--- Pipeline 1 (Trim -> Replace) ---")
    print(f"Entrada: '{texto_entrada}'")
    print(f"Saída  : '{resultado1}'\n")

    # Pipeline 2: ReplaceFilter -> TrimFilter
    pipeline2 = Pipe().add(ReplaceFilter("Software", "Sistemas")).add(TrimFilter())
    # AQUI: troque execute por run
    resultado2 = pipeline2.run(texto_entrada)

    print("--- Pipeline 2 (Replace -> Trim) ---")
    print(f"Entrada: '{texto_entrada}'")
    print(f"Saída  : '{resultado2}'")


if __name__ == "__main__":
    main()