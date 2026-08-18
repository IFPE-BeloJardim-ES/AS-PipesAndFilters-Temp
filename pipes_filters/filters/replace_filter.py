from pipes_filters.filter import Filter

class ReplaceFilter(Filter):
    """Substitui uma palavra por outra""" 

    def __init__(self, target_word: str, replacement_word: str):
        self.target_word = target_word
        self.replacement_word = replacement_word
    def execute(self, data: str) -> str:
        return data.replace(self.target_word, self.replacement_word)