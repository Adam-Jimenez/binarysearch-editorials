"""
Unique Integers in Sorted List

We start at the beginning of the array (i=0). Since the array is sorted, we can binary search for the rightmost occurence of the number i. In this instance, bisect_right will return the first index for which the number is larger than nums[i], so we will jump to the next distinct number.
"""
from bisect import bisect_right
class Solution:
    def solve(self, nums):
        i=0
        ans=0
        while i < len(nums):
            i=bisect_right(nums, nums[i])
            ans+=1
        return ans
        
