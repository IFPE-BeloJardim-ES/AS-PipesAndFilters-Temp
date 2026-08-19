"""Pipes and Filters — exemplo didatico de arquitetura de software."""

from pipes_filters.filter import Filter
from pipes_filters.pipe import Pipe
from pipes_filters.filters.trim_filter import TrimFilter
from pipes_filters.filters.Replace_Filter import ReplaceFilter

__all__ = ["Filter", "Pipe", "TrimFilter", "ReplaceFilter"]
