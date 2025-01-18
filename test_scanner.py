import unittest
from scanner import tokenize


class TestTokenizer(unittest.TestCase):

    def test_basic_numbers(self):
        # Test simple numbers
        expression = "123 45.67 89e2"
        expected = [
            {'type': 'NUMBER', 'value': '123'},
            {'type': 'NUMBER', 'value': '45.67'},
            {'type': 'NUMBER', 'value': '89e2'}
        ]
        self.assertEqual(tokenize(expression), expected)

    def test_function_tokens(self):
        # Test function names
        expression = "add sub mul div mod pow tern"
        expected = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'FUNCTION', 'value': 'sub'},
            {'type': 'FUNCTION', 'value': 'mul'},
            {'type': 'FUNCTION', 'value': 'div'},
            {'type': 'FUNCTION', 'value': 'mod'},
            {'type': 'FUNCTION', 'value': 'pow'},
            {'type': 'FUNCTION', 'value': 'tern'}
        ]
        self.assertEqual(tokenize(expression), expected)

    def test_parentheses_and_comma(self):
        # Test parentheses and comma tokens
        expression = "add(5, mul(3, 4))"
        expected = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '5'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'FUNCTION', 'value': 'mul'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '4'},
            {'type': 'RBRACKET', 'value': ')'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        self.assertEqual(tokenize(expression), expected)

    def test_whitespace_and_comments(self):
        # Test ignoring whitespace and block comments
        expression = "add(  5   ,  mul(3, 4) )  /* comment */"
        expected = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '5'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'FUNCTION', 'value': 'mul'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '4'},
            {'type': 'RBRACKET', 'value': ')'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        self.assertEqual(tokenize(expression), expected)

    def test_invalid_character(self):
        # Test invalid character (should raise error)
        expression = "add(5, 3$)"
        with self.assertRaises(ValueError):
            tokenize(expression)

    def test_ternary_function(self):
        # Test the ternary function
        expression = "tern(1, 2, 3)"
        expected = [
            {'type': 'FUNCTION', 'value': 'tern'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '1'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        self.assertEqual(tokenize(expression), expected)

    def test_nested_functions(self):
        # Test nested function calls
        expression = "add(1, tern(2, 3, mul(4, 5)))"
        expected = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '1'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'FUNCTION', 'value': 'tern'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'FUNCTION', 'value': 'mul'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '4'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '5'},
            {'type': 'RBRACKET', 'value': ')'},
            {'type': 'RBRACKET', 'value': ')'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        self.assertEqual(tokenize(expression), expected)


if __name__ == '__main__':
    unittest.main()
