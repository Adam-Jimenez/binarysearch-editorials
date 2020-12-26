"""
Largest Tree Sum Path

For each node, we can check whats the path with the greatest sum that goes through it by checking the max value of the following possibilites:

- The path starting at the node (if children are negative),
- The path coming from the left child,
- The path coming from the right child,
- The path coming from one children, and going down in the next.

Then, the maximum path coming out of the node can either come from the left, the right or start at the node.
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
            mx=max(mx,l+node.val, r+node.val, l+r+node.val)
            return max(l+node.val,r+node.val,node.val)
        dfs(root)
        return mx
