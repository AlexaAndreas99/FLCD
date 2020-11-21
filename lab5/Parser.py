from Grammar import Grammar


class Configuration:
    def __init__(self):
        self.s = "q"
        self.i = 1
        self.ws = []
        self.ins = []


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.conf = Configuration()
        self.word = None

    def parse(self, word):
        self.word = word.split()
        self.conf.ins = self.grammar.start



    def advance(self):
        self.conf.i += 1
        self.conf.ws.append(self.conf.ins.pop(0))

    def momentary_insuccess(self):
        self.conf.s = 'b'

    def back(self):
        self.conf.i -= 1
        self.conf.ins.insert(0, self.conf.ws.pop())

    def another_try(self):
        aj = self.conf.ws[-1]
        productions = grammar.non_terminal_productions(aj[0])
        if aj[1] < len(productions):
            self.conf.s = 'q'
            self.conf.ws[-1] = (aj[0], aj[1] + 1)
            prod = productions[aj[1] - 1]
            self.conf.ins = productions[aj[1]] + self.conf.ins[len(prod):]
            print(self.conf.ins)
        elif self.conf.i == 1 and aj[0] == self.grammar.start:
            raise Exception()
        else:
            self.conf.ins.insert(0, self.conf.ws.pop()[0])

    def success(self):
        self.conf.s = 'f'

    def expand(self):
        pass


if __name__ == '__main__':
    grammar = Grammar()
    grammar.read_file("g1.txt")
