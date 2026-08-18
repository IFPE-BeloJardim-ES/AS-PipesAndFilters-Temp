from pipes_filters.filter import Filter


class ReplaceFilter (Filter):
    
    def __init__(self, old_word: str, new_word: str):
        self.old_word = old_word
        self.new_word = new_word
    
    def execute(self, data: str) -> str:
        return data.replace(self.old_word, self.new_word)
