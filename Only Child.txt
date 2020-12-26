"""
Only Child

Only child means there is either a left child or a right child but not both - otherwise known as a XOR. 
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return 0
        return self.solve(root.left) + self.solve(root.right) + ((root.left is None) ^ (root.right is None))
