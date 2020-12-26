"""
Class Scheduling

Classic approach to this kind of interval problem.

First we sort by end, guaranteeing that we take the class that will be freed the soonest. Then, we take  classes as long as they don't intersect with the last taken class.
"""
class Solution:
    def solve(self, times):
        times.sort(key=lambda x: x[1])
        last=-1
        ans=0
        for start,end in times:
            if start>last:
                ans+=1
                last=end
        return ans
