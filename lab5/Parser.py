from enum import Enum

from Grammar import Grammar
from Tree import Tree


class ParseException(Exception):
    pass


class States(Enum):
    Q = 'q'
    B = 'b'
    F = 'f'
    E = 'e'

    def __str__(self):
        return self.value


class Configuration:
    def __init__(self):
        self.s = States.Q
        self.i = 1
        self.ws = []
        self.ins = []

    def __str__(self):
        return "({}, {}, {}, {})".format(self.s, self.i, self.ws, self.ins)


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.conf = Configuration()
        self.word = None

    def _debug(self, i):
        s = '[{}] '.format(i)
        for x in self.conf.ws:
            if type(x) == str:
                s += str(x) + ' '
        print(s)

    def parse(self, word):
        self.word = word.split()
        self.conf.ins = [self.grammar.start]

        while self.conf.s not in [States.F, States.E]:
            if self.conf.s == States.Q:
                if len(self.conf.ins) == 0 and self.conf.i == len(self.word) + 1:
                    self.success()
                elif len(self.conf.ins) == 0:
                    self.momentary_insuccess()
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

        return

    def advance(self):
        self.conf.i += 1
        self.conf.ws.append(self.conf.ins.pop(0))
        print('[advance] -> ', self.conf)

    def momentary_insuccess(self):
        self.conf.s = States.B
        print('[mom ins] -> ', self.conf)

    def back(self):
        self.conf.i -= 1
        self.conf.ins.insert(0, self.conf.ws.pop())
        print('[back] -> ', self.conf)

    def another_try(self):
        aj = self.conf.ws[-1]
        productions = self.grammar.non_terminal_productions(aj[0])
        if aj[1] < len(productions):
            self.conf.s = States.Q
            self.conf.ws[-1] = (aj[0], aj[1] + 1)
            prod = productions[aj[1] - 1]
            self.conf.ins = productions[aj[1]] + self.conf.ins[len(prod):]
        elif self.conf.i == 1 and aj[0] == self.grammar.start:
            self.conf.s = States.E
            self.conf.ws.pop()
            self.conf.ins = [aj[0]]
            print('[error] -> ', self.conf)
            raise ParseException()
        else:
            self.conf.ws.pop()
            prod = productions[aj[1] - 1]
            self.conf.ins = [aj[0]] + self.conf.ins[len(prod):]
        print('[ano try] -> ', self.conf)

    def success(self):
        self.conf.s = States.F
        print('[success] -> ', self.conf)

    def expand(self):
        non_terminal = self.conf.ins.pop(0)
        self.conf.ws.append((non_terminal, 1))
        first_production = self.grammar.non_terminal_productions(non_terminal)[0]
        self.conf.ins = first_production + self.conf.ins
        print('[expand] -> ', self.conf)

    def build_tree(self):
        tree = Tree(self.grammar)
        tree.build(self.conf.ws)
        tree.print_table()



if __name__ == '__main__':
    # g1()
    g2()
