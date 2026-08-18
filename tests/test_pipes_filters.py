"""Testes do exemplo. Rodar com:  python -m pytest -q

Repare que cada filtro pode ser testado ISOLADAMENTE, sem montar
pipeline nenhum. Isso e consequencia direta da arquitetura.
"""

import pytest

from pipes_filters import Pipe, Filter
from pipes_filters.filters import UppercaseFilter, ReverseFilter


def test_uppercase_isolado():
    assert UppercaseFilter().execute("abc") == "ABC"


def test_reverse_isolado():
    assert ReverseFilter().execute("abc") == "cba"


def test_pipeline_completo():
    pipe = Pipe().add(UppercaseFilter()).add(ReverseFilter())
    assert pipe.run("abc") == "CBA"


def test_a_ordem_dos_filtros_importa():
    a = Pipe().add(UppercaseFilter()).add(ReverseFilter())
    b = Pipe().add(ReverseFilter()).add(UppercaseFilter())
    # Neste caso especifico o resultado coincide; troque um dos filtros
    # por outro (ex.: TrimFilter) e veja a diferenca aparecer.
    assert a.run("abc") == b.run("abc")


def test_pipe_vazio_nao_altera_o_dado():
    assert Pipe().run("abc") == "abc"


def test_pipe_rejeita_objeto_que_nao_e_filtro():
    with pytest.raises(TypeError):
        Pipe().add("nao sou um filtro")


def test_filtro_novo_nao_exige_alteracao_no_pipe():
    class ExclamacaoFilter(Filter):
        def execute(self, data):
            return data + "!"

    assert Pipe().add(ExclamacaoFilter()).run("oi") == "oi!"


def test_trim_filter_isolado():
    from pipes_filters.filters import TrimFilter
    assert TrimFilter().execute("   Arquitetura   de    Software  ") == "Arquitetura de Software"


def test_replace_filter_isolado():
    from pipes_filters.filters import ReplaceFilter
    assert ReplaceFilter("Software", "Sistemas").execute("Arquitetura de Software") == "Arquitetura de Sistemas"


def test_mask_cpf_filter_isolado():
    from pipes_filters.filters import MaskCpfFilter
    # Testando com formatação
    assert MaskCpfFilter().execute("O CPF é 123.456.789-00.") == "O CPF é ***.***.***-**."
    # Testando sem formatação
    assert MaskCpfFilter().execute("O CPF é 12345678900.") == "O CPF é ***.***.***-**."

