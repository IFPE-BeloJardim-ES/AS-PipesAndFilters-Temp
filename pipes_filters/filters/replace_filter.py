from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
    """Remove espaços das pontas e normaliza espaços internos."""

    def __init__(self, old_word: str, new_word: str) -> None:
        self.old_word = old_word
        self.new_word = new_word

    def execute(self, data: str) -> str:
        return data.replace(self.old_word, self.new_word)
