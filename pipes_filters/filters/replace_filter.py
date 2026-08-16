from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
    """Substitui uma palavra por outra."""

    def __init__(self, old: str, new: str):
        self._old = old
        self._new = new

    def execute(self, data):
        if isinstance(data, str):
            return data.replace(self._old, self._new)
        return data