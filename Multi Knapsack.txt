"""
Multi Knapsack

For each knapsack, we can either take it or not. So we try skipping and taking each value and take the maximal outcome.
"""
from functools import lru_cache
class Solution:
    def solve(self, weights, values, capacity, count):
        @lru_cache(None)
        def dp(i, cap, cnt):
            if i>=len(weights) or cap<0 or cnt<0: return 0
            ans=dp(i+1, cap, cnt)
            if weights[i]<=cap and cnt>=1:
                ans=max(ans,dp(i+1,cap-weights[i],cnt-1)+values[i])
            return ans
        return dp(0,capacity,count)