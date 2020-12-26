"""
K Maximum Sums

We build a prefix sum array to be able to query the sum between two positions easily. Then we compute the sum between every possible interval and put it into a heap. We take the k largest sums from the heap.
"""
from heapq import heappop,heappush
class Solution:
    def solve(self, nums, k):
        ps=[0 for _ in range(len(nums)+1)]
        for i,v in enumerate(nums):
            ps[i+1]=v+ps[i]
        hp=[]
        for i in range(len(ps)):
            for j in range(i+1,len(ps)):
                heappush(hp,-(ps[j]-ps[i]))
        return list(reversed([-heappop(hp) for _ in range(k)]))