"""
Longest Sign Alternating Subsequence

We only need to keep track of the longest subsequence finishing with a negative number or positive number. When the number we reach is negative, we always take the largest positive sequence, and when our number is positive, we take the largest negative sequence and add our number to it.
"""
class Solution:
    def solve(self, nums):
        pos=neg=0
        for n in nums:
            if n<0:
                neg=pos+1
            else:
                pos=neg+1
        return max(pos,neg)