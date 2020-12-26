"""
String Sequence

Constant memory, linear time. We just need to remember the last two elements.
"""
from collections import deque
class Solution:
    def solve(self, s0, s1, n):
        a=deque([s0,s1])
        if n in (0,1): return a[n]
        for i in range(1,n):
            if i&1:
                a.append(a[-1]+a[-2])
            else:
                a.append(a[-2]+a[-1])
            a.popleft()
        return a[-1]
