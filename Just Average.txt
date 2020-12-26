"""
Just Average

We divide all numbers by len(nums)-1, since the average will be the sum of elements divided by the number of elements and we remove one element.

Then we can pick len(nums)-1 numbers from that list and sum them. To check all possibilities, we can do the sum of all values and try subtracting each value to see if we reach k.
"""
from math import isclose
class Solution:
    def solve(self, nums, k):
        n=len(nums)-1
        nums=[x/n for x in nums]
        s=sum(nums)
        return any(isclose(s-x,k) for x in nums)
