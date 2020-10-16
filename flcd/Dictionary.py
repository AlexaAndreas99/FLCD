class Dictionary:
    def __init__(self):
        self.dict = {}

    def put(self, key, value):
        self.dict[key] = value

    def get_free_pos(self):
        if len(self.dict):
            return max(self.dict.keys()) + 1
        else:
            return 0

    def get_key(self, value):
        for i in self.dict:
            if self.dict[i] == value:
                return i
        return False

    def get_value(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return False

    def __str__(self):
        pretty_str = ''
        for i in self.dict:
            pretty_str = pretty_str + str(i) + "-" + str(self.dict[i]) + '\n'

        return pretty_str
