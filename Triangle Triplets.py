"""
Triangle Triplets

To make a valid triangle ABC, A+B>C, A+C>B and B+C>A. If we sort the numbers, we can look at the two smaller numbers to see if they are bigger than the third, since the other constraint will be true if so.

We pick two numbers, and then we look for the highest value for which A+B>C. We can do a binary search for this position using our two picked values.

Then, Since we know all the values for C in range (j,k) are valid, we can add k-j-1 to our answer.
"""
from bisect import bisect_left
class Solution:
    def solve(self, nums):
        nums.sort()
        cnt=0
        for i in range(len(nums)):
            x=nums[i]
            k=i+1
            for j in range(i+1, len(nums)):
                y=nums[j]
                k=bisect_left(nums, x+y, k)
                cnt+=k-j-1
        return cnt%(10**9+7)