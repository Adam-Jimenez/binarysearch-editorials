"""
Largest and Smallest Difference

We sort the numbers because we want to check the values the closest together. Then we use a sliding window to check every possible sublist of length k.
"""
class Solution:
    def solve(self, nums, k):
        nums.sort()
        mn=1e9
        for i in range(len(nums)-k+1):
            mn=min(mn, nums[i+k-1]-nums[i])
        return mn
