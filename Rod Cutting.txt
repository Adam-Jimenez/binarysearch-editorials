"""
Rod Cutting

Memoized solution: we try every possible cut on the rod, and maximize the resulting price.
"""
from functools import lru_cache
class Solution:
    def solve(self, prices, n):
        @lru_cache(None)
        def dp(rem):
            if rem==0: return 0
            return max(dp(rem-i-1)+prices[i] for i in range(rem))
        return dp(n)
