"""
Univalue Tree

Check that the current node equals its children, then recursively check that the same holds for both children.
"""
class Solution:
    def solve(self, root):
        if not root: return True
        if root.left and root.left.val != root.val: return False
        if root.right and root.right.val != root.val: return False
        return self.solve(root.left) and self.solve(root.right)
