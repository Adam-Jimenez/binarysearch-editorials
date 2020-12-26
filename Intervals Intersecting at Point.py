"""
Intervals Intersecting at Point

We count the number of intervals that include the time given as a parameter.
"""
class Solution:
    def solve(self, intervals, time):
        return sum(1 for s,e in intervals if s<=time<=e)
