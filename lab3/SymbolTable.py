from lab3.Dictionary import Dictionary


class SymbolTable:
    def __init__(self):
        self.dict = Dictionary()

    def add(self, value):
        self.dict.add(self.dict.get_free_pos(), value)
        return self.search(value)

    def search(self, value):
        return self.dict.get_key(value)

    def __str__(self):
        return self.dict.__str__()
