import unittest
from code_generation import compile_expression  # Adjust import as needed


class TestCodeGeneration(unittest.TestCase):

    def test_1(self):
        expression = "add(5, mul(3, sub(10, pow(6, 4))))"
        result = compile_expression(expression)
        self.assertEqual(result, "5 + 3 * (10 - 6 ^ 4)")

    def test_2(self):
        expression = "pow(pow(2,3),1)"
        result = compile_expression(expression)
        self.assertEqual(result, "(2 ^ 3) ^ 1")

    def test_3(self):
        expression = "tern(5e2, 2.7,1)"
        result = compile_expression(expression)
        self.assertEqual(result, "5e2?2.7:1")

    def test_4(self):
        expression = "tern(1,tern(2, 3, 4) ,5)"
        result = compile_expression(expression)
        self.assertEqual(result, "1?2?3:4:5")

    def test_5(self):
        expression = "add(add(1,2), 3)"
        result = compile_expression(expression)
        self.assertEqual(result, "1 + 2 + 3")


if __name__ == '__main__':
    unittest.main()
