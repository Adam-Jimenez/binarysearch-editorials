"""
Making List Values Equal

Since we can select a subset, numbers don't need to be adjacent.

Therefore, the constraining factor of this problem will be incrementing the min up to the max value of the array.

O(n) time, O(1) space
"""
class Solution:
    def solve(self, nums):
        return max(nums)-min(nums)