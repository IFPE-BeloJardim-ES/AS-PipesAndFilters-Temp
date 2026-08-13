from pipes_filters.filter import Filter
import unicodedata

class RemoveAcentFilter(Filter):
    def execute(self, data):
        texto_normal = unicodedata.normalize('NFD', data)
        return "".join(
            caractere for caractere in texto_normal
            if unicodedata.category(caractere) != 'Mn')