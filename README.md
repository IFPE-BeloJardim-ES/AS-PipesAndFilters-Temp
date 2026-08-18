# Pipes and Filters — Exemplo em Python

Implementação didática da arquitetura **Pipes and Filters**.

## A ideia

A arquitetura organiza o sistema em componentes modulares. O dado flui através
de **pipes** (tubos) e é processado por **filters** (filtros), o que favorece
flexibilidade, manutenibilidade e extensão do sistema.

```
  entrada ──▶ [ Filtro A ] ──▶ [ Filtro B ] ──▶ [ Filtro C ] ──▶ saída
              └──────────── Pipe conduz o dado ────────────┘
```

## Estrutura do projeto

```
pipes-and-filters-python/
├── pipes_filters/
│   ├── __init__.py
│   ├── filter.py                    # A interface Filter (contrato)
│   ├── pipe.py                      # O Pipe (encadeia e executa)
│   ├── main.py                      # Monta o pipeline
│   └── filters/
│       ├── __init__.py
│       ├── uppercase_filter.py      # Filtro de exemplo
│       └── reverse_filter.py        # Filtro de exemplo
├── tests/
│   └── test_pipes_filters.py
├── ATIVIDADE.txt                    # Enunciado da atividade prática
├── pyproject.toml                   # Equivalente ao pom.xml
└── .gitignore
```

## Os três papéis

| Papel      | Arquivo     | Responsabilidade                           |
| ---------- | ----------- | ------------------------------------------ |
| **Filter** | `filter.py` | Define o contrato: `execute(data) -> data` |
| **Pipe**   | `pipe.py`   | Conduz o dado de um filtro para o próximo  |
| **Main**   | `main.py`   | Escolhe quais filtros usar e em que ordem  |

O ponto central: **o `Pipe` não conhece nenhum filtro concreto.** Ele depende
apenas da interface `Filter`. Por isso, adicionar um filtro novo não exige
alterar o `Pipe` nem os filtros já existentes — apenas o `main.py`, que faz a
montagem. É o Princípio Aberto/Fechado (OCP) na prática.

## Como executar

Requer apenas Python 3.9 ou superior. Nenhuma dependência externa.

```bash
cd pipes-and-filters-python
python -m pipes_filters.main
```

Saída esperada:

```
Pipeline montado : Pipe(UppercaseFilter -> ReverseFilter)
Entrada          : 'Arquitetura de Software'
Saída            : 'ERAWTFOS ED ARUTETIUQRA'
```

## Como rodar os testes

```bash
pip install pytest
python -m pytest -q
```

## Como criar um filtro novo

1. Crie um arquivo em `pipes_filters/filters/`, por exemplo `trim_filter.py`:

```python
from pipes_filters.filter import Filter


class TrimFilter(Filter):
    def execute(self, data: str) -> str:
        return data.strip()
```

2. Exporte-o em `pipes_filters/filters/__init__.py`.
3. Plugue-o no pipeline dentro de `main.py`.

Pronto. Nenhum código existente precisou ser modificado.

## Exercício

O enunciado do exercício para casa está em `ATIVIDADE.txt`. O fluxo é:
fazer um **fork** deste repositório, criar os filtros em uma branch e abrir
um **Pull Request** com as mudanças.

## Respostas

1. O Pipeline 2 deu o mesmo resultado do Pipeline 1? Por quê?

**R: Como o TrimFilter mexe nos espaços e o ReplaceFilter mexe em uma palavra específica que não tem espaços ao redor, a ordem não importa nesse caso. Mas se você usasse o Replace para trocar "Silva" por "Silva " (com espaços), aí a ordem mudaria o resultado**

2. Você precisou abrir o `pipe.py` em algum momento?

**R: Abri apenas para visualiza-lo**

3. Se amanhã fosse preciso adicionar mais dez filtros, quantos arquivos
   que já existem teriam que ser modificados?

**R: Apenas os arquivos `__init__.py` e `main.py`**
