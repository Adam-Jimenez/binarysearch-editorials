"""
Leftmost Deepest Tree Node

Visit each node keeping track of depth in-order, if we ever reach a node with a greater depth, we replace the return value.
"""
class Solution:
    def solve(self, root):
        maxdepth=-1
        maxval=0
        def dfs(node, depth=0):
            nonlocal maxval
            nonlocal maxdepth
            if not node: return
            if depth>maxdepth: 
                maxval=node.val
                maxdepth=depth
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root)
        return maxval
