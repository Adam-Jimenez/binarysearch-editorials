"""
Kth Smallest Element

Using a heap, we can find the desired value in O(k log n).
"""
from heapq import heapify, heappop
class Solution:
    def solve(self, nums, k):
        heapify(nums)
        for i in range(k):
            heappop(nums)
        return heappop(nums)
        # Write your code here
