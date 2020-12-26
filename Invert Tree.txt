"""
Invert Tree

Just do what is told lmao. Don't we just love problems like these?
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def dfs(node):
            if not node: return
            l,r=node.left,node.right
            node.left=dfs(r)
            node.right=dfs(l)
            return node
        return dfs(root)
