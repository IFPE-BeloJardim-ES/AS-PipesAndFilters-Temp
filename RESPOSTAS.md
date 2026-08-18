# Respostas do Exercício - Arquitetura Pipes and Filters

## Perguntas respondidas:

### a) O Pipeline 2 deu o mesmo resultado do Pipeline 1? Por quê?

**Resposta:** Sim, os dois pipelines produziram a mesma saída. Isso ocorre porque neste caso específico, a ordem dos filtros não altera o resultado final. Tanto o `TrimFilter` quanto o `ReplaceFilter` são operações independentes que não se conflitam: o trim remove espaços extras da entrada, e o replace substitui uma palavra. Não importa em qual ordem eles são aplicados, o resultado final é sempre "O cliente Maria da Silva, CPF 123.456.789-00".

### b) Você precisou abrir o `pipe.py` em algum momento?

**Resposta:** Não. O arquivo `pipe.py` permaneceu intocado durante toda a implementação. Seguindo o princípio Aberto/Fechado (OCP), conseguimos adicionar novos filtros apenas criando novos arquivos e editando `main.py` e `filters/__init__.py`. O Pipe, como componente central, permanece estável e fechado para modificação.

### c) Se amanhã fosse preciso adicionar mais dez filtros, quantos arquivos que já existem teriam que ser modificados?

**Resposta:** Apenas 2 arquivos existentes precisariam ser modificados:
1. `pipes_filters/filters/__init__.py` - para importar e exportar os novos filtros
2. `pipes_filters/main.py` - para montar o novo pipeline com os filtros desejados

Nenhum outro arquivo precisaria ser tocado. Demonstrando assim a flexibilidade da arquitetura Pipes and Filters.

---

## Resumo da Implementação

### Filtros criados:

1. **TrimFilter** (`pipes_filters/filters/trim_filter.py`)
   - Remove espaços das pontas do texto
   - Normaliza múltiplos espaços em um único espaço

2. **ReplaceFilter** (`pipes_filters/filters/replace_filter.py`)
   - Substitui uma palavra por outra
   - Recebe as palavras no construtor (não no método execute)
   - Permite encadear múltiplas substituições

### Modificações realizadas:

- Criados 2 novos filtros sem alterar código existente
- Atualizado `pipes_filters/filters/__init__.py` para exportar os novos filtros
- Atualizado `pipes_filters/main.py` para demonstrar dois pipelines diferentes

A arquitetura permanece aberta para extensão e fechada para modificação!
