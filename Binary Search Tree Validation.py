"""
Binary Search Tree Validation

We add a lower and higher bound that every node must respect. When we go left, we reduce our higher bound so that every node to the left must be smaller. When we go right, we augment our lower bound so that every node to the right must be larger.

O(n) Time
O(log n) Space, because a new stack frame is added each recursive call equal to the height of the tree.
"""
class Solution:
    def solve(self, root,lo=float("-inf"), hi=float("inf")):
        return not root or lo<root.val<hi and self.solve(root.left, lo, root.val) and self.solve(root.right, root.val,hi)
