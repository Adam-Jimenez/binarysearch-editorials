"""
One Integer

To minimize the sum, we have to take the smallest numbers available at each iteration. We can use a min-heap to achieve this.
"""
from heapq import heappush, heappop, heapify
class Solution:
    def solve(self, nums):
        heapify(nums)
        ans=0
        while len(nums)>1:
            a,b = heappop(nums), heappop(nums)
            ans+=a+b
            heappush(nums,a+b)
        return ans