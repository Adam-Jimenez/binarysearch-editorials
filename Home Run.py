"""
Home Run

Groupby will group identical consecutive values together, so we can regroup the binary representation of the number and take the longest chain of ones.
"""
from itertools import groupby
class Solution:
    def solve(self, n):
        mx=0
        for bit,group in groupby(bin(n)[2:]):
            if bit == "1":
                mx=max(mx,len(list(group)))
        return mx
