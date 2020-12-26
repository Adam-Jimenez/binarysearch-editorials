"""
Multiset Sum

Top-down DP solution:
For each number, we iterate over multiples of that number. As long as we can fit nums[i] into k, we keep trying to take more, and trying to solve the subproblem with i+1 and k minus the amount of nums[i] we took.

O(n*k) time, O(n) space
"""
from functools import lru_cache
class Solution:
    def solve(self, nums, k):
        @lru_cache(None)
        def dp(i,k):
            if k == 0: return 1
            if i == len(nums): return 0
            ans=0
            j=0
            while j*nums[i]<=k:
                ans+=dp(i+1, k-j*nums[i])
                j+=1
            return ans
        return dp(0, k)
