"""
Connell Sequence

This problem challenges your ability to google Connell sequence and finding this link: https://mathworld.wolfram.com/ConnellSequence.html#:~:text=The%20Connell%20sequence%20is%20the,16%2C%2017%2C%20...
"""
from math import sqrt
class Solution:
    def solve(self, n):
        n+=1
        return 2*n - (1+sqrt(8*n-7))//2
