"""
ZigZag Path

We recursively travel the tree, returning two values for each node: 
1. How far can we get zigzaging to the left child from the current node
2. How can we get zigzaging to the right from the current node

When we bubble up, we can only check how far the left child can zigzag to the right to respect zigzag constraint, and how far the right child can zigzag to the left.

We include the left zigzag of the left child and the right zigzag of the right child because it is possible the longest possible zigzag does not start at the root.

O(n) time, O(depth of the tree, n?) space
"""
class Solution:
    def solve(self, root):
        ans=0
        def rc(node):
            nonlocal ans
            if not node: 
                return 0,0
            l1,r1=rc(node.left)
            l2,r2=rc(node.right)
            ans=max(ans, 1+l2, 1+r1,l1,r2)
            return 1+r1, 1+l2
        rc(root)
        return ans
            