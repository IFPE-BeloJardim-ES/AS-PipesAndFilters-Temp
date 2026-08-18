a) O Pipeline 2 deu o mesmo resultado do Pipeline 1? Por quê?

Não. O Pipeline 1 aplica o TrimFilter primeiro (limpando os espaços) e depois o ReplaceFilter (substituindo palavras), resultando em "O cliente Eng Pedro dos Santos, CPF 123.456.789-00". O Pipeline 2 aplica o ReplaceFilter primeiro, que substitui "Pedro" por "Gustavo" e "de" por "dos" no texto com espaços, e depois o TrimFilter limpa os espaços. O resultado é diferente porque a substituição de palavras pode ser afetada pelos espaços extras no texto original.

b) Você precisou abrir o pipe.py em algum momento?

Não, o Pipe já está pronto para receber qualquer filtro que implemente a interface Filter.

c) Se amanhã fosse preciso adicionar mais dez filtros, quantos arquivos que já existem teriam que ser modificados?

Apenas dois arquivos: main.py (para importar e usar os novos filtros) e filters/__init__.py (para registrar os novos filtros para que possam ser importados do pacote).