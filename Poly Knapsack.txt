"""
Poly Knapsack

This is the same thing as 0/1 knapsacks but when you pick a knapsack, you don't immediately skip to the next one.

For summary, we recursively pick (or not) each knapsack. We memoize using the current weight and the remaining capacity as key.
"""
from functools import lru_cache
class Solution:
    def solve(self, weights, values, capacity):
        @lru_cache(None)
        def dp(i,k):
            if i==len(weights): return 0
            ans=dp(i+1,k)
            if k>=weights[i]:
                ans=max(ans,dp(i,k-weights[i])+values[i])
            return ans
        return dp(0,capacity)
