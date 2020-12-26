"""
Sum of Digit Paths in a Tree

We traverse the tree, keeping a prefix result of the number over the current node. Each time we meet a node, we shift the previous digits by multiplying by 10 and adding the current value. If we reach a leaf (no left or right child), we return the result, otherwise we return the sum of the results of both children (if they exist).
"""
class Solution:
    def solve(self, root):
        def dfs(node,pre):
            cur=pre*10+node.val
            if not node.left and not node.right: return cur
            return sum(dfs(c,cur) for c in (node.left,node.right) if c)
        return dfs(root,0)
        
