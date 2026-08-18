"""Filtros concretos.

Cada filtro mora em seu proprio arquivo. Para criar um novo, basta
adicionar um modulo aqui e exporta-lo na lista abaixo.
"""

from pipes_filters.filters.uppercase_filter import UppercaseFilter
from pipes_filters.filters.reverse_filter import ReverseFilter
from .remove_spaces_filter import RemoveSpacesFilter

__all__ = ["UppercaseFilter", "ReverseFilter"]
