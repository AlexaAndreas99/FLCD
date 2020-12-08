from Grammar import Grammar
from Parser import Parser, ParseException


def g1(g):
    parser = Parser(g)
    try:
        print(parser.parse("a c b c"))
        # print(parser.parse("a c b a"))
    except ParseException:
        print('Error')


def g2(g):
    parser = Parser(g)
    try:
        parser.parse_file("../../compiler-design/Lab 2/pif.out")
        # parser.parse("num y . listen ( y .")
        # parser.parse("seq i from 1 to half with i = i + 1 : kick . end .")
    except ParseException:
        print('Error')


def grammar_menu():
    s = ''
    s += '0. Exit\n'
    s += '1. Grammar 1\n'
    s += '2. Grammar 2\n'
    print(s)


def menu():
    s = ''
    s += '0. Back\n'
    s += '1. Set of non-terminals\n'
    s += '2. Set of terminals\n'
    s += '3. Set of productions\n'
    s += '4. Productions for a given non_terminal\n'
    s += '5. Parse\n'
    print(s)


if __name__ == '__main__':
    while True:
        grammar_menu()
        g = input('>')
        grammar = Grammar()

        if g == '0':
            break
        elif g not in ['1', '2']:
            continue

        grammar.read_file('g' + g + ".txt")

        while True:
            menu()

            i = input('> ')
            if i == '1':
                print(grammar.non_terminals)
            elif i == '2':
                print(grammar.terminals)
            elif i == '3':
                print(grammar.productions)
            elif i == '4':
                non_terminal = input('Give a non terminal > ')
                print(grammar.non_terminal_productions(non_terminal))
            elif i == '5':
                if g == '1':
                    g1(grammar)
                elif g == '2':
                    g2(grammar)
            elif i == '0':
                break
            else:
                print('Command failed successfully')
