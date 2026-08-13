"""Filtros concretos.

Cada filtro mora em seu proprio arquivo. Para criar um novo, basta
adicionar um modulo aqui e exporta-lo na lista abaixo.
Adicionado TrimFilter e ReplaceFilter
"""

from pipes_filters.filters.uppercase_filter import UppercaseFilter
from pipes_filters.filters.reverse_filter import ReverseFilter
from pipes_filters.filters.trim_filter import TrimFilter
from pipes_filters.filters.replace_filter import ReplaceFilter
from pipes_filters.filters.maskcpf_filter import MaskCPFFilter
from pipes_filters.filters.removeacent_filter import RemoveAcentFilter

__all__ = [
    "UppercaseFilter", 
    "ReverseFilter",
    "TrimFilter",
    "ReplaceFilter",
    "MaskCPFFilter",
    "RemoveAcentFilter"
    ]
