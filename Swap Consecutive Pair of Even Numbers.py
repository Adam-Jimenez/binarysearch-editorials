"""
Swap Consecutive Pair of Even Numbers

We keep track of the last even number, and flip them every 2nd time we see an even number.
"""
class Solution:
    def solve(self, nums):
        j,flip=0,False
        for i in range(len(nums)):
            if not nums[i]&1:
                if flip: nums[i],nums[j]=nums[j],nums[i]
                j=i
                flip^=True
        return nums
