import unittest
from astree import ASTNode


class TestASTNode(unittest.TestCase):

    def test_single_node(self):
        # Test a leaf ASTNode
        node = ASTNode('5e2')
        self.assertEqual(node.value, '5e2')
        self.assertIsNone(node.left)
        self.assertIsNone(node.middle)
        self.assertIsNone(node.right)

    def test_binary_node(self):
        # Test a binary ASTNode
        left_child = ASTNode('2.7')
        right_child = ASTNode('1')
        node = ASTNode('add', left_child, right=right_child)

        self.assertEqual(node.value, 'add')
        self.assertEqual(node.left.value, '2.7')
        self.assertEqual(node.right.value, '1')
        self.assertIsNone(node.middle)

    def test_ternary_node(self):
        # Test a ternary function ASTNode
        left_child = ASTNode('5e2')
        middle_child = ASTNode('2.7')
        right_child = ASTNode('1')
        node = ASTNode('tern', left_child, middle=middle_child, right=right_child)

        self.assertEqual(node.value, 'tern')
        self.assertEqual(node.left.value, '5e2')
        self.assertEqual(node.middle.value, '2.7')
        self.assertEqual(node.right.value, '1')

    def test_nested_nodes(self):
        # Test an ASTNode with nested children
        left_child = ASTNode('5e2')
        middle_child = ASTNode('3')
        right_child_left = ASTNode('2.7')
        right_child_right = ASTNode('1')
        right_child = ASTNode('add', left=right_child_left, right=right_child_right)

        node = ASTNode('tern', left_child, middle=middle_child, right=right_child)

        self.assertEqual(node.value, 'tern')
        self.assertEqual(node.left.value, '5e2')
        self.assertEqual(node.middle.value, '3')
        self.assertEqual(node.right.value, 'add')
        self.assertEqual(node.right.left.value, '2.7')
        self.assertEqual(node.right.right.value, '1')

    def test_repr(self):
        # Test the string representation of various ASTNodes
        single_node = ASTNode('5e2')
        self.assertEqual(repr(single_node), "ASTNode(5e2)")

        binary_node = ASTNode('add', ASTNode('2'), right=ASTNode('3'))
        self.assertEqual(repr(binary_node), "ASTNode(add, ASTNode(2), ASTNode(3))")

        ternary_node = ASTNode('tern', ASTNode('1'), middle=ASTNode('2'), right=ASTNode('3'))
        self.assertEqual(repr(ternary_node), "ASTNode(tern, ASTNode(1),ASTNode(2), ASTNode(3))")


if __name__ == '__main__':
    unittest.main()
