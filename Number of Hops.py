"""
Number of Hops

O(n*max(nums)) solution, but with a cheesy optimisation. If dp[j], (the number of hops required to reach nums[j]) is smaller or equal than dp[i], we know everything to the left of it will also be smaller so we don't need to check those values.
"""
class Solution:
    def solve(self, nums):
        dp=[1e9 for _ in nums]
        dp[0]=0
        for i,n in enumerate(nums):
            for j in range(min(i+nums[i], len(nums)-1), i, -1):
                if dp[j]<=dp[i]+1: break
                dp[j] = dp[i]+1
        return dp[-1]
