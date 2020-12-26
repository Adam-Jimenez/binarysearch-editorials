"""
Candy Race

Apparently you can solve this in 1ms, but here's a memoized recursive solution for your soul.
"""
from functools import lru_cache
class Solution:
    def solve(self, candies):
        @lru_cache(None)
        def dfs(i,j):
            if j<i: return 0
            return max(candies[i]-dfs(i+1, j), candies[j]-dfs(i,j-1))
        return dfs(0, len(candies)-1)>0
