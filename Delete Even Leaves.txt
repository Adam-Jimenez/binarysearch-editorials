"""
Delete Even Leaves

Each node is responsible of telling its parent if it is deleting, by returning itself. We do the check after iteration, to respect the constraint that new leaves can be cut as well.
"""
class Solution:
    def solve(self, root):
        def dfs(node):
            if not node: return None
            node.left=dfs(node.left)
            node.right=dfs(node.right)
            if not node.left and not node.right and not node.val&1: return None
            return node
        return dfs(root)
