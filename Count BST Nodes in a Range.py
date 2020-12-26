"""
Count BST Nodes in a Range

If the current node is larger than the higher bound of the interval, every value in the interval will be to the left of the current node because they are smaller.

If the current node is smaller than the lower bound of the interval, every value in the interval will be to the right of the current node because they are larger.

Otherwise, the current value is in the interval and values can be on both sides of the current node.
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        if not root: return 0
        if hi < root.val:
            return self.solve(root.left, lo, hi)
        elif lo >  root.val:
            return self.solve(root.right, lo, hi)
        else:
            return self.solve(root.left, lo, hi) + self.solve(root.right, lo, hi) + 1
