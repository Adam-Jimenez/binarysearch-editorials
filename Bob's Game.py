"""
Bob's Game

We count the number of odd numbers in the list. If we sum two odd numbers together, the result will be even - so the optimal number of moves if the number of odds is divisible by two. 

If there is an odd number of odd numbers - we get stuck with one odd number at the end we can't get rid of.
"""
class Solution:
    def solve(self, nums):
        odds = sum(1 for n in nums if n&1)
        if odds&1: return -1
        return odds//2
