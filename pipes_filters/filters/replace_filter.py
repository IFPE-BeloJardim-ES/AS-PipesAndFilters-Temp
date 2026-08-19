from pipes_filters.filter import Filter

class ReplaceFilter(Filter):

    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new

    def execute (self, data: str) -> str:
        return data.replace(self.old, self.new)