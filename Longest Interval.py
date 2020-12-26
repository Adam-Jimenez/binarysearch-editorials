"""
Longest Interval

We sort intervals, and check if the current interval intersects with the previous one, by checking if the start of the current interval comes before the end of the previous one. 

If so, we update the end of the previous one to the max of the ends of the two intervals. We have to take the max because it is possible the current interval is totally contained by the previous, so that its end comes before the end of the previoius.

Then we remove the redundant interval, and check the max delta in intervals.
"""
class Solution:
    def solve(self, intervals):
        intervals.sort()
        i=1
        while i < len(intervals):
            s,e = intervals[i]
            ps,pe = intervals[i-1]
            if s<=pe:
                intervals[i-1][1]=max(pe, e)
                intervals.pop(i)
            else:
                i+=1
        return max(e-x+1 for x,e in intervals)