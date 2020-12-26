"""
Interval Duration

Literally add every value in the intervals in a set and count unique values.

Don't use this in production.
"""
class Solution:
    def solve(self, intervals):
        s=set()
        for i,j in intervals:
            s.update(range(i,j+1))
        return len(s)
