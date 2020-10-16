from SymbolTable import SymbolTable

if __name__ == '__main__':
    constant_st = SymbolTable()
    variable_st = SymbolTable()

    print("Constants:")
    constant_st.add(1)
    constant_st.add(2)
    constant_st.add(3)
    constant_st.add("abc")
    constant_st.add('c')
    print(constant_st)

    print("Variables:")
    variable_st.add("v1")
    variable_st.add("v2")
    variable_st.add("v3")
    print(variable_st)
