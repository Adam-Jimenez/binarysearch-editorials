"""
Minimum Size of Two Non-Overlapping Intervals

We can build a suffix array containing the minimum cost (defined by the width of the interval) to the right of the current position. Then, for every interval, we can binary search for the position using the end, to find the left most interval that doesn't overlap with the current one. Then, we compute the sum of the current interval and the min to the right of the end and minimize the result.

O(N Log N) time
O(N) space
"""
from bisect import bisect_left
class Solution:
    def solve(self, intervals):
        intervals.sort()
        starts=[s for s,_ in intervals]
        minr=[float("inf") for _ in intervals]
        def cost(interval):
            return interval[1]-interval[0]+1
        minr[-1]=cost(intervals[-1])
        for i in range(len(intervals)-2,-1,-1):
            minr[i]=min(cost(intervals[i]), minr[i+1])
        ans=float("inf")
        for s,e in intervals:
            j = bisect_left(starts,e+1)
            if j<len(starts):
                ans=min(ans, cost([s,e])+minr[j])
        return ans if ans < float("inf") else 0
