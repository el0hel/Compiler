import unittest
from parser import Parser


class TestParser(unittest.TestCase):

    def test_add(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '5'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'add')
        self.assertEqual(ast.left.value, '5')
        self.assertEqual(ast.right.value, '3')

    def test_sub(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'sub'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '10'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '4'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'sub')
        self.assertEqual(ast.left.value, '10')
        self.assertEqual(ast.right.value, '4')

    def test_mul(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'mul'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'mul')
        self.assertEqual(ast.left.value, '2')
        self.assertEqual(ast.right.value, '3')

    def test_div(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'div'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '6'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'div')
        self.assertEqual(ast.left.value, '6')
        self.assertEqual(ast.right.value, '2')

    def test_mod(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'mod'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '7'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'mod')
        self.assertEqual(ast.left.value, '7')
        self.assertEqual(ast.right.value, '3')

    def test_pow(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'pow'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'pow')
        self.assertEqual(ast.left.value, '2')
        self.assertEqual(ast.right.value, '3')

    def test_tern(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'tern'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '1'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'tern')
        self.assertEqual(ast.left.value, '1')
        self.assertEqual(ast.middle.value, '2')
        self.assertEqual(ast.right.value, '3')

    def test_nested_function(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'FUNCTION', 'value': 'mul'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '2'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'RBRACKET', 'value': ')'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '4'},
            {'type': 'RBRACKET', 'value': ')'}
        ]
        parser = Parser(tokens)
        ast = parser.parse()

        self.assertEqual(ast.value, 'add')
        self.assertEqual(ast.left.value, 'mul')
        self.assertEqual(ast.left.left.value, '2')
        self.assertEqual(ast.left.right.value, '3')
        self.assertEqual(ast.right.value, '4')

    def test_missing_closing_bracket(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '5'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'},
            {'type': 'NUMBER', 'value': '3'}
        ]
        parser = Parser(tokens)
        with self.assertRaises(ValueError):
            parser.parse()

    def test_missing_closing_bracket_and_end_tokens(self):
        tokens = [
            {'type': 'FUNCTION', 'value': 'add'},
            {'type': 'LBRACKET', 'value': '('},
            {'type': 'NUMBER', 'value': '5'},
            {'type': 'COMMA', 'value': ','},
            {'type': 'NUMBER', 'value': '3'}
        ]
        parser = Parser(tokens)
        with self.assertRaises(ValueError):
            parser.parse()

    def test_empty_tokens(self):
        parser = Parser([])
        with self.assertRaises(IndexError):
            parser.parse()


if __name__ == '__main__':
    unittest.main()
