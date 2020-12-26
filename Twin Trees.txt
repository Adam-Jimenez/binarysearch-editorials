"""
Twin Trees

We recursively check if the corresponding nodes from each tree are identical. The first two lines handles cases where structure is different.
"""
class Solution:
    def solve(self, n1,n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        return n1.val == n2.val and self.solve(n1.left, n2.left) and self.solve(n1.right, n2.right)
    