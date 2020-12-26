"""
Odd Number of Digits

The number of digits in a number is represented by the its by log base 10. If its even, we have an odd number of digits.
"""
from math import log
class Solution:
    def solve(self, nums):
        return sum(1 for n in nums if not int(log(n,10))&1)
