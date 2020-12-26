"""
Tree Sum

The sum of a tree is the sum of every node and their children.
"""
class Solution:
    def solve(self, root):
        return root.val + self.solve(root.left) + self.solve(root.right) if root else 0
