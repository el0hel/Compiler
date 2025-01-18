from scanner import tokenize
from parser import Parser

# map function names to operator symbols
operator_symbols = {
    'add': '+',
    'sub': '-',
    'mul': '*',
    'div': '/',
    'mod': '%',
    'pow': '^',
    # ternary operator is handled at string level
}

precedence = {
    'tern': 1,
    'add': 2,
    'sub': 2,
    'mul': 3,
    'div': 3,
    'mod': 3,
    'pow': 4
}


def ast_to_string(node):
    if node.left is None and node.right is None:
        # Base case: leaf node (number or function argument)
        return str(node.value)

    # handle ternary function
    if node.value == 'tern':
        if node.middle is None or node.right is None:
            raise ValueError(f"Invalid ternary node structure: {node}")
        op1 = ast_to_string(node.left)
        op2 = ast_to_string(node.middle)
        op3 = ast_to_string(node.right)
        return f"{op1}?{op2}:{op3}"

    # Handle binary function calls
    if node.right is not None and node.middle is None:
        left_expr = ast_to_string(node.left)
        right_expr = ast_to_string(node.right)

        if node.value in operator_symbols:
            # checking if both child nodes are operators
            if node.right.value in operator_symbols and node.left.value in operator_symbols:
                opright = node.right.value
                opleft = node.left.value
                opright_precedence = precedence[opright]
                opleft_precedence = precedence[opleft]
                parent_precedence = precedence[node.value]

                # bracketing according to precedence
                if opright_precedence > parent_precedence > opleft_precedence:
                    return f"({left_expr}) {operator_symbols[node.value]} {right_expr}"
                elif opright_precedence < parent_precedence < opleft_precedence:
                    return f"{left_expr} {operator_symbols[node.value]} ({right_expr})"
                elif opright_precedence < parent_precedence and opleft_precedence < parent_precedence:
                    return f"({left_expr}) {operator_symbols[node.value]} ({right_expr})"
                else:
                    return f"{left_expr} {operator_symbols[node.value]} {right_expr}"

            # checking if right node is an operator
            elif node.right.value in operator_symbols:
                opright = node.right.value
                opright_precedence = precedence[opright]
                parent_precedence = precedence[node.value]

                # bracketing according to precedence,
                if (parent_precedence == 2 and opright_precedence == 2) or opright_precedence > parent_precedence:
                    # no bracketing if symbols are + +, - -, + -, - + or if right node has higher precedence than
                    # parent node
                    return f"{left_expr} {operator_symbols[node.value]} {right_expr}"
                else:
                    return f"{left_expr} {operator_symbols[node.value]} ({right_expr})"

            # checking if left node is an operator
            elif node.left.value in operator_symbols:
                opleft = node.left.value
                opleft_precedence = precedence[opleft]
                parent_precedence = precedence[node.value]

                if (parent_precedence == 2 and opleft_precedence == 2) or opleft_precedence > parent_precedence:
                    # same logic as for right node
                    return f"{left_expr} {operator_symbols[node.value]} {right_expr}"
                else:
                    return f"({left_expr}) {operator_symbols[node.value]} {right_expr}"


        else:
            raise ValueError(f"Unknown operator: {node.value}")

        return f"{left_expr} {operator_symbols[node.value]} {right_expr}"

    # in case of unexpected structure
    raise ValueError(f"Unhandled AST Node structure: {node}")


# compile expression into a string with proper bracketing showing precedence
def compile_expression(expression):
    tokens = tokenize(expression)  # tokenise the input
    parser = Parser(tokens)  # parse tokens into an AST
    ast = parser.parse()  # get the AST
    return ast_to_string(ast)  # create the output string


expr = " add(5, mul(3, sub(10, pow(6, 4))))"
final = compile_expression(expr)
print(final)

#Input: add(5, mul(3, sub(10, 6)))
#Output: 5 + 3 * (10 - 6)
