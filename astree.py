# class to represent a node in AST
class ASTNode:
    # constructor
    def __init__(self, value, left=None, middle=None, right=None):
        self.value = value
        self.left = left  # left child
        self.middle = middle  # for ternary functions
        self.right = right  # right child

    def __repr__(self):
        # representing ASTNode as string for debugging
        if self.middle is not None:
            return f"ASTNode({self.value}, {self.left},{self.middle}, {self.right})"
        elif self.right is not None:
            return f"ASTNode({self.value}, {self.left}, {self.right})"
        elif self.left is not None:
            return f"ASTNode({self.value}, {self.left})"
        else:
            return f"ASTNode({self.value})"
