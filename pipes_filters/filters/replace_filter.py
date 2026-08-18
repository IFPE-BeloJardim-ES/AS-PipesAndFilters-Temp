from pipes_filters.filter import Filter

class ReplaceFilter(Filter):
    def __init__(self, old: str, new: str):
        self._old = old
        self._new = new

    def execute(self, data: str) -> str:
        return data.replace(self._old, self._new)