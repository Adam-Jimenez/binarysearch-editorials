"""
Inorder Successor

First step is to find t, so we go left if t is smaller, right if t is larger.

When we find t, if it has a right node, we go right then completely left to find the smallest value greater than t.
If there is no right node, we need to remember the last time we went left in the tree when searching for t, it is the last value that was greater than t (the hi parameter).
"""
class Solution:
    def solve(self, root, t,hi=None):
        if t<root.val:
            return self.solve(root.left,t,root.val)
        elif t>root.val:
            return self.solve(root.right,t,hi)
        else:
            if root.right:
                n=root.right
                while n.left: n=n.left
                return n.val
            return hi
