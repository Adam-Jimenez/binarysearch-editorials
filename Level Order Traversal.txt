"""
Level Order Traversal

Simplest form of breadth-first search. Use a double-ended queue to do popleft() in constant time.
"""
from collections import deque
class Solution:
    def solve(self, root):
        ans=[]
        q=deque([root])
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return ans

    