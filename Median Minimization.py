"""
Median Minimization

2 lazy to do the math myself, let python do it for me lel
"""
from statistics import median
class Solution:
    def solve(self, nums):
        nums.sort()
        return abs(median(nums[0::2])-median(nums[1::2]))
