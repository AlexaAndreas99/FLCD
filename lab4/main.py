from lab4.FiniteAutomata import FiniteAutomata


def menu():
    print("0.Exit")
    print("1.Set of states")
    print("2.Alphabet")
    print("3.Transitions")
    print("4.Initial state")
    print("5.Final states")
    print("6.Verify a sequence")


def test():
    try:
        print(fa.accepts('001110'))  # true
        print(fa.accepts('001111'))  # false
        print(fa.accepts('00111100'))  # false
    except KeyError:
        print("False")


if __name__ == '__main__':
    fa = FiniteAutomata()
    fa.reader()

    while True:
        print()
        menu()
        i = input()
        if i == '1':
            fa.print_states()
        elif i == '2':
            fa.print_input_symbols()
        elif i == '3':
            fa.print_transitions()
        elif i == '4':
            fa.print_initial_state()
        elif i == '5':
            fa.print_final_states()
        elif i == '6':
            s = input("Sequence: ")
            try:
                res = fa.accepts(s)
            except KeyError:
                res = False
            if res:
                print("Sequence is accepted by the FA")
            else:
                print("Sequence is not accepted by the FA")
        elif i == '0':
            break
        else:
            print("Command not found, please try again!")

    # test()
