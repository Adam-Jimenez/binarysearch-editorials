"""
Minimum Initial Value for Positive Prefix Sums

We need the lowest value in the prefix sum array to be >= 1, so we find the minimum, negate it and add one.
"""
class Solution:
    def solve(self, nums):
        pf = [0]
        for n in nums:
            pf.append(pf[-1]+n)
        return -min(pf) + 1