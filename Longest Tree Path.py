"""
Longest Tree Path

One way to do this efficiently is for every node, count the amount of nodes under them in a bottom-up fashion. 

For every node, the longest path going through that node is the deepest from the left to the deepest to the right (plus one, to include the node).
"""
class Solution:
    def solve(self, root):
        mx=0
        def dfs(node):
            nonlocal mx
            if not node: return 0
            deepest_left=dfs(node.left)
            deepest_right=dfs(node.right)
            mx=max(mx, deepest_left+deepest_right+1)
            return 1+max(deepest_left, deepest_right)
        dfs(root)
        return mx