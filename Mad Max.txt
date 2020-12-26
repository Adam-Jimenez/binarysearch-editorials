"""
Mad Max

The trick to doing this in O(n) is to use a queue of maxes. When we encounter a new value, we remove all those lower than it and add it to the queue, so that the elements in the queue are always sorted decreasingly, and the front of the queue is always the current max.

More visuals here: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""
from collections import deque
class Solution:
    def solve(self, nums, k):
        q=deque()
        ans=[]
        for i,n in enumerate(nums):
            if q and q[0]<=i-k: q.popleft()
            while q and n>=nums[q[-1]]:
                q.pop()
            q.append(i)
            if i>=k-1: ans.append(nums[q[0]])
        return ans
