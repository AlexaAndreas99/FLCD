from Dictionary import Dictionary


class SymbolTable:
    def __init__(self):
        self.dict = Dictionary()

    def add(self, value):
        self.dict.put(self.dict.get_free_pos(), value)
        return self.dict.get_free_pos()

    def search(self, value):
        return self.dict.get_key(value)

    def __str__(self):
        return self.dict.__str__()
