"""
Largest Equivalent Set of Pairs

We want to track the difference between the two sets - each number put into set B will be subtracted and each number put into set A will be added. If both sets are equal the difference will be 0. We then bubble up the sum reached.
"""
from functools import lru_cache
class Solution:
    def solve(self, nums):
        @lru_cache(None)
        def dp(i, bal):
            if i==len(nums):
                return 0 if bal == 0 else -1e9
            return max(
                dp(i+1, bal),
                dp(i+1, bal+nums[i])+nums[i],
                dp(i+1, bal-nums[i])
                )
        return dp(0,0)
