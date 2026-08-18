from pipes_filters.filter import Filter


class ReplaceFilter(Filter):

    def __init__(self, ant_palavra, nova_palavra):
        self.ant_palavra = ant_palavra
        self.nova_palavra = nova_palavra

    def execute(self, data):
        return data.replace(self.ant_palavra, self.nova_palavra)