"""
Scrum Journeyman

We can treat start of intervals and end of intervals separately, using a new "events" array. Each time a new interval starts, we increment a running count variable, and each time an interval ends, we decrement it. 

Each time the running count changes, we commit the state to the answer array. Be careful to eliminate empty ranges, and ranges when the running count is zero.
"""
class Solution:
    def solve(self, intervals, jobs):
        ev=[]
        for s,e in intervals:
            ev.append((s,1))
            ev.append((e,-1))
        ev.sort()
        cnt=0
        last=-1
        ans=[]
        for t, inc in ev:
            if t != last and cnt != 0:
                ans.append([last,t,cnt])
            cnt+=inc
            last=t
        return ans