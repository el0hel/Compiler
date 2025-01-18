# tokenize an expression
import re


def tokenize(expression):
    # defining a list of regular expressions to match token types (grammar)
    token_patterns = [
        (r'[ \t\n]+', None),  # skipping whitespace
        (r'/\*.*?\*/', None),  # skipping block comments
        (r'\d+(\.\d+)?([eE][+-]?\d+)?', 'NUMBER'),  # numbers
        (r'\b(add|sub|mul|div|mod|pow|tern)\b', 'FUNCTION'),  # function names
        (r'\(', 'LBRACKET'),
        (r'\)', 'RBRACKET'),
        (r',', 'COMMA'),
    ]

    tokens = []  # empty list to store tokens
    position = 0  # current position in expression

    # looping through entire expression
    while position < len(expression):
        match = None  # no match yet

        # checking each pattern and its type to so see if it matches current part of expression
        for pattern, token_type in token_patterns:
            possible_token = re.compile(pattern)  # compile pattern
            match = possible_token.match(expression, position)
            if match:
                if token_type:
                    # adding it to token list if it matches the grammar
                    tokens.append({'type': token_type, 'value': match.group(0)})
                position = match.end()  # update position
                break  # stop checking other patterns
        if not match:
            raise ValueError(f"Tokenise error: unexpected character {expression[position]}")

    return tokens
