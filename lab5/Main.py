from Grammar import Grammar
from Parser import Parser, ParseException


def g1(g):
    parser = Parser(g)
    try:
        parser.parse("a c b c")
        # print(parser.parse("a c b a"))
    except ParseException:
        print('Error')


def g2(g):
    parser = Parser(g)
    try:
        parser.parse("num y . listen ( y ) .")
        # parser.parse("seq i from 1 to half with i = i + 1 : kick . end .")
    except ParseException:
        print('Error')


def menu():
    s = ''
    s += '0. Exit\n'
    s += '1. Set of non-terminals\n'
    s += '2. Set of terminals\n'
    s += '3. Set of productions\n'
    s += '4. Productions for a given non_terminal\n'
    s += '5. Parse\n'
    print(s)


if __name__ == '__main__':
    while True:
        g = 'g2'
        grammar = Grammar()
        grammar.read_file(g + ".txt")

        print('')
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
            if g == 'g1':
                g1(grammar)
            elif g == 'g2':
                g2(grammar)
        elif i == '0':
            break
        else:
            print('Command failed successfully')
