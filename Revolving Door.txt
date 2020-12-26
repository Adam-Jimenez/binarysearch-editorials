"""
Revolving Door

I don't remember what i was doing but it kinda works xDD
"""
from collections import defaultdict
class Solution:
    def solve(self, requests):
        buckets=defaultdict(lambda: [[], []])
        last=1
        lasttime=-1
        for time, direction in requests:
            buckets[time][direction].append("")
        ans=[]
        for time in sorted(buckets.keys()):
            if time > lasttime:
                last = 1
                lasttime=time
            while buckets[time][last]:
                buckets[time][last].pop()
                ans.append([lasttime, last])
                lasttime+=1
            if buckets[time][last^1]:
                last ^= 1
                while buckets[time][last]:
                    buckets[time][last].pop()
                    ans.append([lasttime, last])
                    lasttime+=1
        return ans
                
