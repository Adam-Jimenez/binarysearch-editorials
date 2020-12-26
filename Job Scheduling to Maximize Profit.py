"""
Job Scheduling to Maximize Profit

For each job i, we can either skip it, or take it and jump to the next job starting at e (we sort to be able to binary search for the next job).
"""
from functools import lru_cache
from bisect import bisect_left
class Solution:
    def solve(self, intervals):
        intervals.sort()
        starts=[s for s,_,_ in intervals]
        @lru_cache(None)
        def dp(i):
            if i >= len(intervals): return 0
            s,e,p = intervals[i]
            ans = dp(i+1)
            j = bisect_left(starts,e)
            ans2 = dp(j) + p
            return ans if ans > ans2 else ans2
        return dp(0)
