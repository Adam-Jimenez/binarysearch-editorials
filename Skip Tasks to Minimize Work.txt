"""
Skip Tasks to Minimize Work

Simplified bottom-up DP: since our recurrence relation only depends on dp[i-1] and dp[i-2], we only need to keep those two values in memory as a,b and update them sequentially.
"""
class Solution:
    def solve(self, nums):
        if len(nums) <= 1: return 0
        a,b=nums[0],nums[1]
        for i in range(2,len(nums)):
            a,b = b, nums[i] + min(a,b)
        return min(a,b)
