"""
Counting Maximal Value Roots in Binary Tree

We can recursively get the maximum descendant for each node, and while bubbling up, we check if the current node is greater than the max of its descendants, and increment our answer if so.

O(n) time
O(h) space, height of tree
"""
class Solution:
    def solve(self, root):
        ans=0
        def rc(node):
            if not node: return -1e9
            nonlocal ans
            l=rc(node.left)
            r=rc(node.right)
            if node.val >= l and node.val >= r:
                ans+=1
            return max(node.val,l,r)
        rc(root)
        return ans
