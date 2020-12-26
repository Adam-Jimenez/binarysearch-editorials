"""
Height Balanced Tree

for every node in the tree, the absolute difference of the height of its left subtree and the height of its right subtree is less than two. and children are balanced as well.
"""
class Solution:
    def solve(self, root):
        def dfs(node,d=0):
            if not node: return True, d-1
            left_bal, ld = dfs(node.left,d+1)
            right_bal, rd = dfs(node.right, d+1)
            return left_bal and right_bal and abs(ld-rd) < 2, max(d,ld,rd)
        return dfs(root)[0]
