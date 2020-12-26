"""
Leaf Equivalent Trees

We can use a generator to iterate through the leaves of each tree.
Then we can zip all corresponding leaves and check their equality.
"""
from itertools import zip_longest as zipl
class Solution:
    def solve(self, root0, root1):
        return all(x==y for x,y in zipl(leaves(root0), leaves(root1)))
def leaves(node):
    if not node.left and not node.right: yield node.val
    if node.left: yield from leaves(node.left)
    if node.right: yield from leaves(node.right)
