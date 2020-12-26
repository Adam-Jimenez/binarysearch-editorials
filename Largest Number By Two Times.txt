"""
Largest Number By Two Times

Using a "max" heap, we can retrieve the max elements in O(ln) time.
"""
import heapq
class Solution:
    def solve(self, nums):
        nums=[-x for x in nums]
        heapq.heapify(nums)
        return heapq.heappop(nums) < 2*heapq.heappop(nums)
        # Write your code here
