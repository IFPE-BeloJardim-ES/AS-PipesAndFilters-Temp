from pipes_filters.filter import Filter


class TrimFilter(Filter):

    def execute(self, data):
        return ' '.join(data.strip().split())