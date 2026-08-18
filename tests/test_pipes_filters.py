"""Testes do exemplo. Rodar com:  python -m pytest -q

Repare que cada filtro pode ser testado ISOLADAMENTE, sem montar
pipeline nenhum. Isso e consequencia direta da arquitetura.
"""

import pytest

from pipes_filters import Pipe, Filter
from pipes_filters.filters import UppercaseFilter, ReverseFilter
from pipes_filters.filters import TrimFilter, ReplaceFilter

def test_uppercase_isolado():
    assert UppercaseFilter().execute("abc") == "ABC"

def test_reverse_isolado():
    assert ReverseFilter().execute("abc") == "cba"

def test_trim_isolado():
    filtro = TrimFilter()
    assert filtro.execute("   Arquitetura   de    Software  ") == "Arquitetura de Software"

def test_replace_isolado():
    filtro = ReplaceFilter("Software", "Sistemas")
    assert filtro.execute("Arquitetura de Software") == "Arquitetura de Sistemas"

def test_pipeline_completo():
    pipe = Pipe().add(UppercaseFilter()).add(ReverseFilter())
    assert pipe.run("abc") == "CBA"

def test_a_ordem_dos_filtros_importa():

    # Pipe A limpa os espaços e depois troca o espaço que sobrou por traço
    pipe_a = Pipe().add(TrimFilter()).add(ReplaceFilter(" ", "-"))


    # Pipe B troca os espaços por traços primeiro e depois tenta limpar
    pipe_b = Pipe().add(ReplaceFilter(" ", "-")).add(TrimFilter())
    
    # " a  b " -> Pipe A vira "a-b"
    # " a  b " -> Pipe B vira "-a--b-"
    assert pipe_a.run(" a  b ") != pipe_b.run(" a  b ")

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