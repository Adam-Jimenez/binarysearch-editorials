"""
Left Side View of a Tree

We apply BFS to the tree, in such a way that we iterate one level at a time using for _ in range(len(q)). We take the first node in each level for our answer.
"""
from collections import deque
class Solution:
    def solve(self, root):
        
        q=deque([root])
        ans=[]
        while q:
            first=True
            for _ in range(len(q)):
                cur=q.popleft()
                if first:
                    ans.append(cur.val)
                for c in (cur.left, cur.right):
                    if c: q.append(c)
                first=False
        return ans
