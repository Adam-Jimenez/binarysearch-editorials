"""
Interval Union

Intersection happens when the end of the previous intervals overlaps the start of the current one. In that case, we can create a new interval comprising the minimum start and the max ending.
"""
class Solution:
    def solve(self, intervals):
        intervals.sort()
        ans=[]
        for start,end in intervals:
            if ans and ans[-1][1]>=start:
                prev_start,prev_end = ans[-1]
                ans[-1]=(min(prev_start,start),max(prev_end,end))
            else:
                ans.append((start,end))
        return ans
