# Exercício para casa — Arquitetura Pipes and Filters

**Disciplina:** Arquitetura de Software
**Professor:** Matheus Barbosa

Este exercício não vale nota. Ele existe para você entender, escrevendo
código de verdade, por que essa arquitetura é usada — e de quebra treinar o
fluxo de fork, branch e Pull Request, que é como se trabalha em equipe no
mundo real.

## O que você vai fazer

Você vai adicionar funcionalidades novas a um sistema pronto SEM alterar
nenhuma linha do código que já existe.

Se ao final você conseguir fazer isso, terá visto na prática o Princípio
Aberto/Fechado: um sistema aberto para extensão e fechado para modificação.

## Passo 1 — Pegar o projeto

Repositório original:

```
https://github.com/IFPE-BeloJardim-ES/AS-PipesAndFilters-Temp
```

1. Clique em "Fork" no canto superior direito. Isso cria uma cópia do
   projeto na SUA conta do GitHub.

2. Clone o SEU fork (não o original):

   ```bash
   git clone https://github.com/SEU-LOGIN/AS-PipesAndFilters-Temp.git
   ```

   ```bash
   cd AS-PipesAndFilters-Temp
   ```

3. Crie uma branch para o seu trabalho:

   ```bash
   git checkout -b filtros-seunome
   ```

## Passo 2 — Entender o que já existe

Rode o projeto antes de escrever qualquer coisa:

```bash
python -m pipes_filters.main
```

Depois leia estes três arquivos, nesta ordem. São curtos.

| Arquivo                   | O que é                                                                      |
| ------------------------- | ---------------------------------------------------------------------------- |
| `pipes_filters/filter.py` | a interface Filter. É o contrato: todo filtro tem um método `execute(data)`. |
| `pipes_filters/pipe.py`   | o Pipe. Ele guarda uma lista de filtros e passa o dado de um para o outro.   |
| `pipes_filters/main.py`   | monta o pipeline: escolhe quais filtros usar e em que ordem.                 |

Repare em uma coisa: o Pipe não conhece nenhum filtro específico. Ele só
conhece a interface. Guarde essa observação, ela é o ponto do exercício.

## A única regra

> Não altere `filter.py`, `pipe.py`, `uppercase_filter.py` nem `reverse_filter.py`.

Você só pode criar arquivos novos e editar dois: o `main.py` e o
`filters/__init__.py` (onde os filtros são registrados).

Se em algum momento você sentir vontade de mexer no `pipe.py` para o seu
filtro funcionar, pare. Anote o motivo e traga para a aula, essa é
provavelmente a parte mais interessante do exercício.

## Parte obrigatória

### Crie dois filtros

1. **TrimFilter**

   Remove os espaços das pontas e transforma sequências de espaços em
   um espaço só.

   ```
   entrada:  "   Arquitetura   de    Software  "
   saída:    "Arquitetura de Software"
   ```

2. **ReplaceFilter**

   Substitui uma palavra por outra. Atenção: as palavras devem ser
   informadas na CRIAÇÃO do filtro, não no execute. Ou seja, o filtro
   é usado assim:

   ```python
   ReplaceFilter("Software", "Sistemas")
   ```

   Se você precisou mudar a assinatura do execute, algo saiu do rumo —
   o Pipe chama execute com um argumento só.

Cada filtro em seu próprio arquivo, dentro de `pipes_filters/filters/`,
seguindo o padrão de nomes que já está lá.

### Monte dois pipelines no main.py

Use este texto nos dois:

```
"   O   cliente João  da  Silva,  CPF 123.456.789-00  "
```

Pipeline 1: use o TrimFilter e o ReplaceFilter.
Pipeline 2: os mesmos dois filtros, em ordem trocada.

Imprima a entrada e a saída de cada um.

### Responda no README do seu fork (duas ou três linhas bastam)

a) O Pipeline 2 deu o mesmo resultado do Pipeline 1? Por quê?
- Resposta: Deu o mesmo resultado, pois os filtros só trocaram a ordem de "Concertar", mas no final fazem a mesma coisa.

b) Você precisou abrir o `pipe.py` em algum momento?
- Resposta: Sim, mas só para olhar e confrimar os nomes das definições.

c) Se amanhã fosse preciso adicionar mais dez filtros, quantos arquivos
que já existem teriam que ser modificados?
- Resposta: Dois arquivos, isso sem contar os novos 10.

## Parte opcional

Nada aqui é obrigatório. Faça o que achar interessante.

### Mais filtros. Escolha os que quiser:

| Filtro                | Descrição                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `RemoveAccentsFilter` | Remove a acentuação preservando as letras. Dica: módulo `unicodedata` da biblioteca padrão.                                                      |
| `CensorFilter`        | Recebe uma lista de palavras proibidas na criação e troca cada uma por asteriscos.                                                               |
| `MaskCpfFilter`       | Encontra CPFs no texto (formatados ou não) e substitui por `***.***.***-**`. Use regex.                                                          |
| `WordCountFilter`     | Devolve a quantidade de palavras. Cuidado: a saída deixa de ser texto. O que acontece com o filtro que vier depois?                              |
| `TokenizerFilter`     | Divide o texto em uma lista de palavras. Mesmo alerta do anterior.                                                                               |
| `ValidationFilter`    | Se a entrada for vazia ou só espaços, interrompe o processamento. Como interromper é decisão sua — escreva no PR por que escolheu daquele jeito. |
| Um filtro seu         | Qualquer coisa útil que não esteja na lista.                                                                                                     |

### Testes

O arquivo `tests/test_pipes_filters.py` já tem alguns exemplos. Escreva
testes para os filtros que você criou.

```bash
pip install pytest
```

```bash
python -m pytest -q
```

Enquanto escreve, note que você consegue testar cada filtro sozinho,
sem montar pipeline nenhum.

### Desafios de verdade

Nenhum destes encaixa bem na arquitetura atual. É exatamente esse o
ponto. Se tentar algum, traga o problema para a aula.

1. Um filtro que precise LEMBRAR do que processou antes (por exemplo,
   contar quantas vezes foi executado). Filtro deveria guardar estado?

2. Um filtro que mande a saída para dois caminhos ao mesmo tempo.
   O Pipe é linear. Como você mudaria isso?

3. Um filtro que leia de um arquivo (início do fluxo) e outro que
   escreva em arquivo (fim do fluxo). Eles ainda são "filtros"?

4. Processar um arquivo de 5 GB sem carregar tudo na memória.
   Pesquise: geradores (`yield`) em Python.

## Modelo de filtro — copie e adapte

Arquivo: `pipes_filters/filters/meu_filtro.py`

```python
from pipes_filters.filter import Filter


class MeuFiltro(Filter):
    """Descreva aqui o que o filtro faz."""

    def execute(self, data):
        # transforme o dado e devolva o resultado
        return data
```

Registre em `pipes_filters/filters/__init__.py`:

```python
from pipes_filters.filters.meu_filtro import MeuFiltro

__all__ = ["UppercaseFilter", "ReverseFilter", "MeuFiltro"]
```

Use no `main.py`:

```python
pipeline = Pipe().add(MeuFiltro())
```

Duas coisas que valem lembrar enquanto escreve:

- Um filtro faz UMA coisa só. Se o nome dele tem "e" no meio
  (TrimAndUppercaseFilter), provavelmente são dois filtros.

- O filtro DEVOLVE o dado, não imprime na tela. Quem imprime é o main.

## Passo 3 — Enviar o Pull Request

```bash
git add .
```

```bash
git commit -m "Adiciona TrimFilter e ReplaceFilter"
```

```bash
git push origin filtros-seunome
```

Depois, no GitHub:

1. Abra o seu fork. Vai aparecer um aviso com o botão
   "Compare & pull request". Clique nele.

2. Confirme que a comparação está indo do SEU fork para o repositório
   original, e não o contrário.

3. No título do PR, coloque seu nome:

   ```
   Exercicio Pipes and Filters - Seu Nome
   ```

4. Na descrição, escreva:
   - quais filtros você criou
   - as respostas das perguntas a, b e c
   - se fez algo da parte opcional, o que foi
   - qualquer dúvida ou coisa que travou no caminho

5. Clique em "Create pull request".

Não se preocupe se o PR não estiver perfeito. Ele é o ponto de partida da
conversa, não o produto final e é assim que funciona no trabalho também.

## Antes de enviar, confira

- [ ] O projeto roda: `python -m pipes_filters.main`
- [ ] Os dois filtros estão cada um em seu arquivo
- [ ] O `main.py` tem os dois pipelines e imprime entrada e saída
- [ ] Nenhum filtro imprime na tela por conta própria
- [ ] `filter.py` e `pipe.py` estão intactos
- [ ] As respostas a, b e c estão na descrição do PR

Dúvida trava o exercício? Abra uma issue no repositório original ou traga
na próxima aula. Perguntar cedo é melhor do que travar sozinho.
