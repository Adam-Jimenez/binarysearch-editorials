"""
Sum Tree

Edge cases:
- null node: nothing is equal to the sum of nothing and nothing, so return True
- Leaves: if no children, return True

Then compute the sum and check that all subnodes respect the constraint.
"""
class Solution:
    def solve(self, root):
        if not root: return True
        if not root.left and not root.right: return True # leaf
        s=0
        if root.left:
           s+=root.left.val
        if root.right:
           s+=root.right.val
        return s==root.val and self.solve(root.left) and self.solve(root.right)