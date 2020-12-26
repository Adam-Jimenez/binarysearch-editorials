"""
Split List

For every position in the array, you save the maximum value up to that point, and the minimum value coming after it. For the constraints to be respected, the maximum before the current position must be less than the minimum in the numbers following it.
"""
class Solution:
    def solve(self, nums):
        mx=[-1e9 for _ in nums]
        mn=[1e9 for _ in nums]
        mx[0] = nums[0]
        mn[-1] = nums[-1]
        for i in range(1,len(nums)):
            mx[i]=max(nums[i],mx[i-1])
        for i in range(len(nums)-2,-1,-1):
            mn[i]=min(nums[i],mn[i+1])
        return any(mx[i]<mn[i+1] for i in range(len(nums)-1))
