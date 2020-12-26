"""
Equal Piles

The only way to all numbers to be the same is to all become equal to the smallest number.

For any number to become equal to the smallest number, they must first go through every number in between.

So we can sum the number of unique numbers in between the current number and the smallest to get the answer.
"""
class Solution:
    def solve(self, nums):
        d={x:i for i,x in enumerate(sorted(set(nums)))}
        return sum(d[x] for x in nums)
        