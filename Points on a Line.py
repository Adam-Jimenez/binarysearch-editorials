"""
Points on a Line

O(N^2) solution: first we sort the points so the slopes are processed in the same relative order for all points.

Then, we iterate over each point, setting them as the relative origin against which we will compute the slope for each point.

For each point, we check all the point to its right - compute the slope (dx/dy). To avoid problems with division by zero, we can simplify leave the fraction under the form of a tuple, simplifying it by dividing by the greatest common divisor of the numerator and denominator. One edge case is 0/0 (two identical points) where the gcd will be 0, then we can use 1 as a gcd instead.

We count the largest amount of points sharing the same slope, relative to a previous point.
"""
from math import gcd
from collections import defaultdict
class Solution:
    def solve(self, coordinates):
        ans=0
        coordinates.sort()
        for i,(ox,oy) in enumerate(coordinates):
            cnt=defaultdict(int)
            for j in range(i+1, len(coordinates)):
                cx,cy = coordinates[j]
                dx = cx-ox
                dy = cy-oy
                ngcd = max(gcd(dx,dy),1)
                dx //= ngcd
                dy //= ngcd
                cnt[(dx,dy)]+=1
                ans=max(ans,cnt[(dx,dy)])
        return ans+1
