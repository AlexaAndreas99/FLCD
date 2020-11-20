class Grammar():
    def __init__(self):
        self.non_terminals = []
        self.terminals = []
        self.start = None
        self.productions = {}

    def read_file(self, filename):
        with open(filename, 'r') as f:
            self.non_terminals = f.readline().strip().split(', ')
            self.terminals = f.readline().strip().split(', ')
            self.start = f.readline().strip()

            for i in range(len(self.non_terminals)):
                non_terminal, productions = f.readline().split(' -> ')

                if non_terminal not in self.productions.keys():
                    self.productions[non_terminal] = []

                productions = productions.split(' | ')
                for prod in productions:
                    self.productions[non_terminal].append(prod.strip().split())

    def non_terminal_productions(self, nt):
        if nt not in self.productions.keys():
            return None
        return self.productions[nt]


if __name__ == '__main__':
    g = Grammar()
    g.read_file('g1.txt')
    print(g.non_terminals)
    print(g.terminals)
    print(g.start)
    print(g.productions)
    print(g.non_terminal_productions("S"))
