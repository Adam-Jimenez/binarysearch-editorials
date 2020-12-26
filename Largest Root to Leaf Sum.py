"""
Largest Root to Leaf Sum

Compute the sum of the subtrees, take the max sum and add the current value.
"""
class Solution:
    def solve(self, root):
        if not root: return 0
        return root.val + max(self.solve(root.left), self.solve(root.right))
