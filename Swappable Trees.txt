"""
Swappable Trees

We try swapping at each node, and checking for equality at each equivalent node.

Not sure about time complexity, but I think it's O(n) because for each node we have two possible sub-states, either keep trees the same or flip the trees. It has to be under O(n^2), because that is the number of possible unique inputs to the function.

Edit: seems to be O(n^2)
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):
        def dfs(root0, root1):
            if not root0 and not root1: return True
            if not root0 or not root1: return False
            return root0.val == root1.val and (
                (dfs(root0.left, root1.left) and dfs(root0.right, root1.right)) or
                (dfs(root0.left, root1.right) and dfs(root0.right, root1.left)) 
                )
        return dfs(root0, root1)
