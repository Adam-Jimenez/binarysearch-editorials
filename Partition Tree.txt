"""
Partition Tree

We recurse on each node verifying its leaf status by checking if it has any children. If not, we increment leaf counter otherwise non-leaf counter.
"""
class Solution:
    def solve(self, root):
        leaves=0
        notleaves=0
        def dfs(node):
            nonlocal leaves
            nonlocal notleaves
            if not node: return
            if not node.left and not node.right: 
                leaves+=1
            else:
                notleaves+=1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return (leaves,notleaves)
