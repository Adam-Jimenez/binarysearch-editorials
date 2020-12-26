"""
Changing Directions

We compute the slopes by doing nums[i+1] - nums[i].

Then, to check for changes from positive to negative slopes or the reverse, we can multiply adjacent slopes: only a positive and a negative will give a value less than zero, so then we can count the number of results lower than zero.
"""
class Solution:
    def solve(self, nums):
        s = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
        return sum(1 for i in range(len(s)-1) if s[i+1]*s[i]<0)