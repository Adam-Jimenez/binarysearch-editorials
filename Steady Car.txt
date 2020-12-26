"""
Steady Car

We create a list of speeds by subtracting position i by position i-1. We use groupby to group equal contiguous elements. We return the longest such contiguous group.
"""
from itertools import groupby
class Solution:
    def solve(self, positions):
        return max(map(lambda x: len(list(x[1])), groupby([abs(positions[i]-positions[i-1]) for i in range(1,len(positions))])))+1
