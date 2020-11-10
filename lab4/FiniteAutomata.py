import re


class FiniteAutomata:

    def __init__(self):
        self.states = []
        self.input_symbols = []
        self.initial_state = []
        self.final_states = []
        self.transitions = {}
        # Transitions structure
        # {A:{'1':'B', '0':'A'},
        #  B:{'1':'B', '0':'C'},
        #  C:{}}
        self.is_dfa = True

    def reader(self):
        f = open("FA.in", "r")
        row = 0
        for x in f:
            result = []
            line = re.split(' |\n', x)
            for i in line:
                result.append(i)
            while '' in result:
                result.remove('')
            self.add_to_fa(result, row)
            row += 1

        for i in self.final_states:
            if i not in self.transitions.keys():
                self.transitions[i] = {}

    def add_to_fa(self, res, i):
        if i == 0:
            self.states = res
        elif i == 1:
            self.input_symbols = res
        elif i == 2:
            self.initial_state = res
        elif i == 3:
            self.final_states = res
        else:
            if res[0] not in self.transitions.keys():
                self.transitions[res[0]] = {res[1]: res[3]}
            else:
                if res[1] in self.transitions[res[0]].keys():
                    self.is_dfa = False
                self.transitions[res[0]][res[1]] = res[3]

    def accepts(self, s):
        if self.is_dfa:
            state = self.initial_state[0]
            for c in s:
                if c not in self.transitions[state]:
                    raise KeyError
                state = self.transitions[state][c]

            return state in self.final_states
        else:
            print("FA is not deterministic")

    def print_transitions(self):
        print(self.transitions)

    def print_states(self):
        print(self.states)

    def print_input_symbols(self):
        print(self.input_symbols)

    def print_initial_state(self):
        print(self.initial_state)

    def print_final_states(self):
        print(self.final_states)

    def print_is_dfa(self):
        print(self.is_dfa)
