"""
Subtree

Each time the root and the target match, we check if they all share common children from that point on, otherwise we keep exploring the root.
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if not root or not target: return not root and not target
        elif root.val == target.val:
            if self.solve(root.left,target.left) and self.solve(root.right, target.right): return True
        return self.solve(root.left,target) or self.solve(root.right,target)
