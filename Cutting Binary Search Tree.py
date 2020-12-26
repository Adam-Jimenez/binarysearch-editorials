"""
Cutting Binary Search Tree

HERE'S JOHNNY!

If the node if outside the range, exclude it. Then test each of his children. ez pz 
"""
class Solution:
    def solve(self, root, lo, hi):
        if not root: return
        if lo > root.val:
            return self.solve(root.right,lo,hi)
        if hi < root.val:
            return self.solve(root.left,lo,hi)
        root.right=self.solve(root.right,lo,hi)
        root.left=self.solve(root.left,lo,hi)
        return root
