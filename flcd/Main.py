from SymbolTable import SymbolTable
import re
import Scanner

if __name__ == '__main__':
    filename = "p1err.txt"
    scanner = Scanner.Scanner(filename)
    scanner.reader()
    scanner.pretty_pif()
    print()
    scanner.pretty_vst()
    scanner.pretty_cst()
