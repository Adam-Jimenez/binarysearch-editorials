"""
Longest Even Value Path

For each node, we check the longest path that comes from a child, goes through the node and back down to the other child. When returning to the parent node, we must pick the longest path coming from the child nodes.
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        mx=0
        def dfs(node):
            nonlocal mx
            if not node: return 0
            l=dfs(node.left)
            r=dfs(node.right)
            if node.val%2==1: return 0
            mx=max(mx, 1+l+r)
            return max(l,r)+1
        dfs(root)
        return mx
            
    