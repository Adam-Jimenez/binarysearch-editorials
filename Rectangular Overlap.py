"""
Rectangular Overlap

Sexy one-liner solution. Iterate over each dimension individually, and check that the maximum of the start of the interval for each rectangle is less than the minimum of the ends.
"""
class Solution:
    def solve(self, rect0, rect1):
        return all(max(s) < min(e) for s,e in zip(zip(rect0[:2],rect1[:2]), zip(rect0[2:],rect1[2:])))
