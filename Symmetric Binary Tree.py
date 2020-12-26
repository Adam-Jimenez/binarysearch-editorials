"""
Symmetric Binary Tree

We iterate the left child and the right child in reverse order, checking that each corresponding value is equal.
"""
from itertools import zip_longest as zipl
class Solution:
    def solve(self, root):
        return all(x==y for x,y in zipl(it(root), it(root,False)))

def it(node, left=True):
    if not node: return
    yield from it(node.left if left else node.right, left)
    yield node.val
    yield from it(node.right if left else node.left, left)