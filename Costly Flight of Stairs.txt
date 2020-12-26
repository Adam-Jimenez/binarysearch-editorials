"""
Costly Flight of Stairs

DP solution, where the optimal way to reach dp[i] is `$dp[i]+ \min_{x=1..k} dp[i-x]$`
If we were to iterate over every predecessor of dp[i], the complexity would be of O(n*k), because we would have to iterate over the k previous values.
But, using a min-queue, we can reduce this complexity down to O(n), because we can lookup the min in a sliding window in constant time.

O(n) time, O(k) space
"""
from collections import deque
class Solution:
    def solve(self, stairs, k):
        q=deque([(stairs[0],0)]) # (cost, i)
        for i in range(1,len(stairs)):
            while i-q[0][1]>k:
                q.popleft()
            curcost=q[0][0]+stairs[i]
            while q and curcost<=q[-1][0]:
                q.pop()
            q.append((curcost,i))
        return q[-1][0]