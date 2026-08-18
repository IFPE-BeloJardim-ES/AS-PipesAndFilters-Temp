import re
from pipes_filters.filter import Filter
class TrimFilter(Filter):
    """Remove os espaços"""
    
    def execute(self, data: str) -> str:
        trimmed_data = data.strip()
        return re.sub(r'\s+', ' ', trimmed_data)