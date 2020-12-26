"""
Sum of the Deepest Nodes

We can do BFS, and only keep the sum of the last layer we iterate through.
"""
from collections import defaultdict,deque
class Solution:
    def solve(self, root):
        if not root: return 0
        q=deque([root])
        ans=0
        while q:
            ans=0
            for _ in range(len(q)):
                cur=q.popleft()
                ans+=cur.val
                for c in (cur.left, cur.right): 
                    if c: q.append(c)
        return ans