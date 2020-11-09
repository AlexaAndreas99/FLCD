from lab3 import Scanner

if __name__ == '__main__':
    filename = "lab3/p1err.txt"
    scanner = Scanner.Scanner(filename)
    scanner.reader()
    scanner.pretty_pif()
    print()
    scanner.pretty_vst()
    scanner.pretty_cst()
    # fa = FiniteAutomata()
    # fa.reader()
    # fa.print_transitions()

    # try:
    #     print(fa.accepts('001110'))  # true
    #     print(fa.accepts('001111'))  # false
    #     print(fa.accepts('00111100'))  # false
    # except KeyError:
    #     print("False")
    #print(5 ** 637 % 2549)
    #print(2*16*256*1811*1707*342*289%2549)
