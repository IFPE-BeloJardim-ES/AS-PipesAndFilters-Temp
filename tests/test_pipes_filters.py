"""Testes do exemplo.

Cada filtro pode ser testado isoladamente, e o Pipe segue sendo o orquestrador
do encadeamento.
"""

import pytest

from pipes_filters import Filter, Pipe
from pipes_filters.filters import (
    ReplaceFilter,
    ReverseFilter,
    TrimFilter,
    UppercaseFilter,
    WordCountFilter,
)


def test_uppercase_filter():
    filtro = UppercaseFilter()

    assert filtro.execute("abc") == "ABC"
    assert filtro.execute("Cliente João") == "CLIENTE JOÃO"


def test_reverse_filter():
    filtro = ReverseFilter()

    assert filtro.execute("abc") == "cba"
    assert filtro.execute("Pipe") == "epiP"


def test_trim_filter():
    filtro = TrimFilter()

    assert filtro.execute("  abc  ") == "abc"
    assert filtro.execute("  a   b   c  ") == "a b c"
    assert filtro.execute("\t  Arquitetura   de    Software  \n") == "Arquitetura de Software"


def test_replace_filter():
    filtro = ReplaceFilter("cliente", "usuário")

    assert filtro.execute("o cliente chegou") == "o usuário chegou"
    assert filtro.execute("cliente cliente") == "usuário usuário"
    assert filtro.execute("sem alvo") == "sem alvo"


def test_word_count_filter():
    filtro = WordCountFilter()

    assert filtro.execute("abc") == 1
    assert filtro.execute("a b c") == 3
    assert filtro.execute("  O   cliente João  da  Silva,   CPF 123.456.789-00   ") == 7


def test_pipeline_com_trim_e_replace():
    pipe = Pipe().add(TrimFilter()).add(ReplaceFilter("cliente", "usuário"))

    assert pipe.run("  O   cliente João  da  Silva,   CPF 123.456.789-00   ") == (
        "O usuário João da Silva, CPF 123.456.789-00"
    )


def test_pipeline_com_word_count_no_final():
    pipe = Pipe().add(TrimFilter()).add(ReplaceFilter("cliente", "usuário")).add(WordCountFilter())

    assert pipe.run("  O   cliente João  da  Silva,   CPF 123.456.789-00   ") == 7


def test_a_ordem_dos_filtros_importa():
    entrada = "  O   cliente João  da  Silva,   CPF 123.456.789-00   "

    pipeline_a = Pipe().add(TrimFilter()).add(ReplaceFilter("cliente", "usuário"))
    pipeline_b = Pipe().add(ReplaceFilter("cliente", "usuário")).add(TrimFilter())

    assert pipeline_a.run(entrada) == pipeline_b.run(entrada)


def test_pipe_vazio_nao_altera_o_dado():
    assert Pipe().run("abc") == "abc"


def test_pipe_rejeita_objeto_que_nao_e_filtro():
    with pytest.raises(TypeError):
        Pipe().add("nao sou um filtro")


def test_novo_filtro_nao_exige_alteracao_no_pipe():
    class ExclamacaoFilter(Filter):
        def execute(self, data):
            return data + "!"

    assert Pipe().add(ExclamacaoFilter()).run("oi") == "oi!"
