class Node:
    def __init__(self, value, child, rs):
        self.value = value
        self.child = child
        self.right_sibling = rs

    def __str__(self):
        return "({}, {}, {})".format(self.value, self.child, self.right_sibling)


class Tree:
    def __init__(self, grammar):
        self.root = None
        self.grammar = grammar
        self.crt = 1

    def build(self, ws):
        self.root = self.build_recursive(ws, 1)
        return self.root

    def build_recursive(self, ws, n):
        if n <= 0:
            return None
        elem = ws.pop(0)
        if type(elem) == str:
            node = Node(elem, None, None)
            node.right_sibling = self.build_recursive(ws, n - 1)
            return node
        else:
            node = Node(elem[0], None, None)
            no_productions = len(self.grammar.non_terminal_productions(elem[0])[elem[1] - 1])
            node.child = self.build_recursive(ws, no_productions)
            node.right_sibling = self.build_recursive(ws, n - 1)
            return node

    def print_table(self):
        self.bfs(self.root)

    def bfs(self, node, father_crt=None, left_sibling_crt=None):
        if node is None:
            return []
        print("{} | {} | {} | {}".format(self.crt, node.value, father_crt, left_sibling_crt))

        crt = self.crt
        self.crt += 1

        if left_sibling_crt is not None:
            return [[node.child, crt, None]] + self.bfs(node.right_sibling, father_crt, crt)
        else:
            children = [[node.child, crt, None]] + self.bfs(node.right_sibling, father_crt, crt)
            for child in children:
                self.bfs(*child)

    def __str__(self):
        string = ""
        node = self.root
        while node is not None:
            string += str(node)
            node = node.right_sibling
        return string
