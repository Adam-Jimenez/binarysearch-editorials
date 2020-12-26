"""
Count Exact Sum

DP solution similar to knapsack.

We recursively iterate over each number, trying to pick each number for our subset if possible and skipping it.
We return one if we reach a subset of sum k, and we memoize everything.
"""
from functools import lru_cache
MOD=(10**9)+7
class Solution:
    def solve(self, nums, k):
        @lru_cache(None)
        def dp(i,k):
            if k==0: return 1
            if i==len(nums): return 0
            ans=dp(i+1,k)
            if k>=nums[i]:
                ans+=dp(i+1,k-nums[i])
            return ans
        return dp(0,k)%MOD
