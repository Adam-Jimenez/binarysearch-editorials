"""
Birthday Party

Dequeue's rotate function helps us emulate skipping over children.
"""
from collections import deque
class Solution:
    def solve(self, n, k):
        q=deque(range(n))
        while len(q)>1:
            q.rotate(-k)
            q.popleft()
        return q[0]