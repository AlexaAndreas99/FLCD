from enum import Enum

from Grammar import Grammar


class ParseException(Exception):
    pass


class States(Enum):
    Q = 'q'
    B = 'b'
    F = 'f'
    E = 'e'


class Configuration:
    def __init__(self):
        self.s = States.Q
        self.i = 1
        self.ws = []
        self.ins = []


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.conf = Configuration()
        self.word = None

    def parse(self, word):
        self.word = word
        self.conf.ins = [self.grammar.start]

        while self.conf.s not in [States.F, States.E]:
            if self.conf.s == States.Q:
                if len(self.conf.ins) == 0 and self.conf.i == len(self.word) + 1:
                    self.success()
                else:
                    if self.conf.ins[0] in self.grammar.non_terminals:
                        self.expand()
                    else:
                        if self.conf.i <= len(self.word) and self.conf.ins[0] == self.word[self.conf.i - 1]:
                            self.advance()
                        else:
                            self.momentary_insuccess()
            else:
                if self.conf.s == States.B:
                    if self.conf.ws[-1] in self.grammar.terminals:
                        self.back()
                    else:
                        self.another_try()

        return self.conf.s == States.F

    def advance(self):
        self.conf.i += 1
        self.conf.ws.append(self.conf.ins.pop(0))

    def momentary_insuccess(self):
        self.conf.s = States.B

    def back(self):
        self.conf.i -= 1
        self.conf.ins.insert(0, self.conf.ws.pop())

    def another_try(self):
        aj = self.conf.ws[-1]
        productions = grammar.non_terminal_productions(aj[0])
        if aj[1] < len(productions):
            self.conf.s = States.Q
            self.conf.ws[-1] = (aj[0], aj[1] + 1)
            prod = productions[aj[1] - 1]
            self.conf.ins = productions[aj[1]] + self.conf.ins[len(prod):]
        elif self.conf.i == 0 and aj[0] == self.grammar.start:
            self.conf.s = States.E
            raise ParseException()
        else:
            self.conf.ins.insert(0, self.conf.ws.pop()[0])

    def success(self):
        self.conf.s = States.F

    def expand(self):
        non_terminal = self.conf.ins.pop(0)
        self.conf.ws.append((non_terminal, 1))
        first_production = self.grammar.non_terminal_productions(non_terminal)[0]
        self.conf.ins = first_production + self.conf.ins


if __name__ == '__main__':
    grammar = Grammar()
    grammar.read_file("g1.txt")
    parser = Parser(grammar)
    print(parser.parse("acbc"))
    #print(parser.parse("acba"))
