import re
import string
from SymbolTable import SymbolTable


class Scanner:
    def __init__(self, filename):
        self.filename = filename
        self.pif = []  # (token , pos in st) pairs
        self.reserved = self.get_tokens()
        self.constant_st = SymbolTable()
        self.variable_st = SymbolTable()

    def get_tokens(self):
        res = []
        f = open("token.txt", "r")
        for x in f:
            line = re.split(' |\n', x)
            for i in line:
                res.append(i)
        while '' in res:
            res.remove('')
        return res

    def reader(self):
        f = open(self.filename, "r")
        row = 0
        for x in f:
            result = []
            line = re.split(' |\n', x)
            for i in line:
                result.append(i)
            while '' in result:
                result.remove('')

            self.scanner(result, row)
            row += 1
        self.pretty_pif()

    def scanner(self, result, line):

        for token in result:
            if token in self.reserved and token != '':
                self.pif.append((token, 0))
            elif self.is_identifier(token):
                index = self.variable_st.add(token)
                self.pif.append((token, index))
            elif self.is_constant(token):
                index = self.constant_st.add(token)
                self.pif.append((token, index))
            else:
                if token != '':
                    print("Lexical Error on line", line, token)

    def pretty_pif(self):
        for i in self.pif:
            print(i[0], "->", i[1])

    def is_identifier(self, token):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lower_letters = list(string.ascii_lowercase)
        upper_letters = list(string.ascii_uppercase)
        if token == '':
            return 0
        if token[0] in numbers:
            return 0

        if token[0] in lower_letters or token[0] in upper_letters:
            for i in range(1, len(token)):
                if token[i] not in numbers and token[i] not in lower_letters and token[i] not in upper_letters:
                    return 0
            return 1

        return 0

    def is_constant(self, token):
        first_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        sign = ['+', '-']
        if token == '':
            return 0
        # caracter and string
        if token[0] == "\"" and token[-1] == "\"" or token[0] == "\'" and token[-1] == "\'":
            return 1

        # intreg
        if token[0] == '0' and len(token) == 1:
            return 1

        if token[0] == '0' or (token[0] in sign and token[1] == '0'):  # +0, -0
            return 0

        if token[0] in first_char:
            if len(token) == 1:
                return 1
            for i in range(1, len(token)):
                if token[i] not in numbers:
                    return 0
            return 1
        return 0
