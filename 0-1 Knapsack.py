"""
0-1 Knapsack

For each knapsack, we can either take it or not, so we try both possibilities recursively as long as we have sufficient capacity. We memoize using @lru_cache.
"""
from functools import lru_cache
class Solution:
    def solve(self, weights, values, capacity):
        @lru_cache(None)
        def dp(i, cap):
            if i>=len(weights): return 0
            ans=dp(i+1, cap)
            if cap>=weights[i]:
                ans=max(ans, dp(i+1, cap-weights[i])+values[i])
            return ans
        return dp(0,capacity)
