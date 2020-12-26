"""
Maximum Consecutive Difference

Why is this is hard? Lawrence plz fix.                   
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        ans=0
        for i in range(len(nums)-1):
            ans=max(ans, nums[i+1]-nums[i])
        return ans
