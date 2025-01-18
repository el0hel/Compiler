from astree import ASTNode


class Parser:
    precedence = {
        'tern': 1,
        'add': 2,
        'sub': 2,
        'mul': 3,
        'div': 3,
        'mod': 3,
        'pow': 4
    }

    # constructor to initialise parser with tokens
    def __init__(self, tokens):
        self.tokens = tokens  # tokens passed from scanner
        self.pos = 0

    # start parsing expression
    def parse(self):
        return self.parse_expression(0)

    def parse_expression(self, parent_precedence):
        # parse an expression with a given parent precedence

        token = self.tokens[self.pos]  # read current token

        # parse a number token
        if token['type'] == 'NUMBER':
            self.pos += 1
            left = ASTNode(token['value'])  # create AST node

        # parse a function token
        elif token['type'] == 'FUNCTION':
            left = self.parse_function(parent_precedence)  # parse the function

        else:
            raise ValueError(f"Invalid token: {token}")

        # handle operators based on precedence
        while self.pos < len(self.tokens):
            token = self.tokens[self.pos]

            # if token is an operator, check if its precedence is higher than or equal
            # to the parent operator's precedence
            if token['type'] == 'FUNCTION' and token['value'] in self.precedence:
                operator = token['value']
                operator_precedence = self.precedence[operator]

                if operator_precedence < parent_precedence:
                    break  # if operator has lower precedence than the parent operator, stop parsing

                self.pos += 1

                # parse the right operand using current operator's precedence
                right = self.parse_expression(operator_precedence)

                # create AST node for the operator with its left and right operands
                left = ASTNode(operator, left, right)

            else:
                break  # stop loop if token is not an operator

        return left  # return constructed node for an expression

    def parse_function(self, parent_precedence):
        # parse function calls
        function_token = self.tokens[self.pos]  # getting token
        self.pos += 1
        function_name = function_token['value']  # getting name of function

        # for ternary operator
        if function_name == 'tern':
            return self.parse_ternary_function()
        # for binary functions
        return self.parse_binary_function(function_name, parent_precedence)

    def parse_binary_function(self, function_name, parent_precedence):
        # parse binary functions
        if self.tokens[self.pos]['type'] == 'LBRACKET':
            self.pos += 1  # consume '('
            left = self.parse_expression(
                max(parent_precedence, self.precedence[function_name]))  # parse left operand
            if self.tokens[self.pos]['type'] == 'COMMA':
                self.pos += 1  # consume comma
                right = self.parse_expression(self.precedence[function_name])  # parse right operand

                # check for closing bracket
                if self.pos < len(self.tokens) and self.tokens[self.pos]['type'] == 'RBRACKET':
                    self.pos += 1  # consume ')'
                    return ASTNode(function_name, left=left, right=right)  # create AST node for function
                else:
                    raise ValueError(f"Missing closing bracket after {function_name} arguments.")
            else:
                raise ValueError(f"Missing second argument for {function_name} function.")
        else:
            raise ValueError(f"Invalid token after function {function_name}.")

    def parse_ternary_function(self):
        # parse ternary functions
        if self.tokens[self.pos]['type'] == 'LBRACKET':
            self.pos += 1  # consume (
            op1 = self.parse_expression(0)  # parse 1st operand
            if self.tokens[self.pos]['type'] == 'COMMA':
                self.pos += 1  # consume ,
                op2 = self.parse_expression(0)  # parse 2nd operand
                if self.tokens[self.pos]['type'] == 'COMMA':
                    self.pos += 1  # consume ,
                    op3 = self.parse_expression(0)
                    if self.tokens[self.pos]['type'] == 'RBRACKET':
                        self.pos += 1  # consume )
                        return ASTNode('tern', op1, op2, op3)  # create AST node
                    else:
                        raise ValueError(f"Missing closing bracket after ternary function arguments.")
                else:
                    raise ValueError(f"Missing third argument for ternary function.")
            else:
                raise ValueError(f"Missing second argument for ternary function.")
        else:
            raise ValueError(f"Invalid token after ternary function.")
