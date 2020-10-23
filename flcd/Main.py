from SymbolTable import SymbolTable
import re
import Scanner

if __name__ == '__main__':
    filename = "p1.txt"
    scanner = Scanner.Scanner(filename)
    scanner.reader()
