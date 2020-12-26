"""
24

Fix for my last solution, where there was a bug where the root of the expression tree for a part of the array was lost.
"""
import operator
from itertools import permutations, product
OPERATORS=["+","-","*","/"]
class Solution:
    def solve(self, nums):
        for operators in product(OPERATORS,repeat=3):
            for order in permutations(range(3)):
                if compute(operators,order,nums): return True
        return False

class Node:
    fn={
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.floordiv
    }
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
        self.parent=None
    def compute(self):
        if not self.left and not self.right:
            return self.value
        return Node.fn[self.value](self.left.compute(),self.right.compute())
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        if not self.left and not self.right: return str(self.value)
        return f"({self.value} {str(self.left)} {str(self.right)})"

def compute(operators,order,nums):
    nums=[Node(n) for n in nums]
    for idx in order:
        op = operators[idx]
        left = nums[idx]
        while left.parent: left = left.parent
        right = nums[idx+1]
        while right.parent: right = right.parent
        node=Node(op, left, right)
        left.parent, right.parent = node,node
    try:
        return node.compute() == 24
    except ZeroDivisionError:
        return False