from pipes_filters.filter import Filter


class ReplaceFilter(Filter):
    def __init__(self, old_text: str, new_text: str):
        self.old_text = old_text
        self.new_text = new_text

    def execute(self, data: str) -> str:
        return data.replace(self.old_text, self.new_text)