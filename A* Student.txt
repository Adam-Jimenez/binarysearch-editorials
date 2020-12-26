"""
A* Student

We process the jobs in sorted order according to deadlines, to maximize the time we have to complete a set of deadlines.
Then, we iterate recursively on the jobs. For each job we have two options: either to take it or not to take it. 
If we don't take it, the days don't go forward, but if we do, we add the duration of the job to the current day.

We return the maximum of credits we reach from the subproblems.
"""
from functools import lru_cache
class Solution:
    def solve(self, deadlines, credits, durations):
        jobs=sorted(zip(deadlines,durations,credits))
        @lru_cache(None)
        def dp(i=0, day=0):
            if i >= len(jobs): return 0
            ans=dp(i+1,day)
            deadline,duration,credit=jobs[i]
            if day+duration-1 <= deadline:
                ans=max(ans, dp(i+1, day+duration)+credit)
            return ans
        return dp()
