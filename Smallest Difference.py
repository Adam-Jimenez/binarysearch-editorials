"""
Smallest Difference

Given a random selection of numbers, there is two ways to optimize the answer:
1. Change the lower bound (min) in the hopes that is goes higher and tightens the interval
2. Change the upper bound (max) in the hopes that is goes lower and tightens the interval

If we sort the lists and start with all the minimum values - we eliminate one possibility. Now the only way to get a better answer is to change the min value, because the max value can only go upwards.

We can use a heap to continually extract the min value from all lists, and save each intermediate results. 
"""
from heapq import heapify, heappop, heappush
class Solution:
    def solve(self, lists):
        for l in lists:
            l.sort()
        hp = [(l[0],0,i) for i,l in enumerate(lists)]
        heapify(hp)
        hi = max(l[0] for l in lists)
        ans=float('inf')
        while True:
            cur_min,idx,list_idx = heappop(hp)
            ans=min(ans, hi-cur_min)
            if idx == len(lists[list_idx])-1: break
            next_val = lists[list_idx][idx+1]
            if next_val>hi: hi=next_val
            heappush(hp, (next_val, idx+1, list_idx))
        return ans
            