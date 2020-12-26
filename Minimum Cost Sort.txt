"""
Minimum Cost Sort

To compute the cost, compute the sum of the difference of corresponding numbers in the original list and the sorted ones. Take the minimum.
"""
class Solution:
    def solve(self, nums):
        return min(
            sum(abs(x-y) for x,y in zip(nums,sorted(nums))),
            sum(abs(x-y) for x,y in zip(nums,sorted(nums, reverse=True)))
        )
