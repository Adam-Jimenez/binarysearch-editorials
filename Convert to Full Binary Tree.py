"""
Convert to Full Binary Tree

We check the cases where only one child is not None, and we return its value if so.

Note that we do the recursion at the start of the function, so that we proceed in a bottom-up fashion. 
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return
        root.left=self.solve(root.left)
        root.right=self.solve(root.right)
        if root.left is not None and root.right is None:
            return root.left
        if root.left is None and root.right is not None:
            return root.right
        return root
