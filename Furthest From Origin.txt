"""
Furthest From Origin

We can take the absolute difference between Ls and Rs to get the distance from the origin, then add ?s to it.
"""
class Solution:
    def solve(self, s):
        return abs(s.count("L")-s.count("R"))+s.count("?")
