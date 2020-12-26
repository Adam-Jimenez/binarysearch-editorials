"""
Split Product

DP solution: we try every number between 1 and n as a product, then solve for the remaining sub-problem.

O(n^2), because there are n unique states, and each state has a cost of n because of the loop.
"""
from functools import lru_cache
class Solution:
    def solve(self, n):
        @lru_cache(None)
        def dp(n):
            if n == 0: return 1
            ans=0
            for i in range(1,n+1):
                ans=max(ans, i*dp(n-i))
            return ans
        return dp(n)
