"""
Interval Intersection

Assuming there is an intersection between all intervals, the rightmost start will be less than the leftmost end, and they will define the smallest intersecting interval.
"""
class Solution:
    def solve(self, intervals):
        s,e=zip(*intervals)
        return max(s), min(e) 
