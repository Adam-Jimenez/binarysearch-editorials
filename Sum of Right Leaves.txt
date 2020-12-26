"""
Sum of Right Leaves

Return the value if we meet the required conditions, otherwise we will eventually return 0. Use a boolean to check if we are a right child.
"""
class Solution:
    def solve(self, root):
        def dfs(node, right=False):
            if not node: return 0
            if not node.left and not node.right and right: return node.val
            return dfs(node.left, False)+dfs(node.right, True)
        return dfs(root)
