"""
Count of Sublists with Same First and Last Values

We record the position for each number. The number of sublist where we pick n values is n*(n+1)/2, the arithmetic series 1+2+3+...+n

Ex:  say a number n is at 3 positions
we can pick 1-1, 1-2, 1-3, 2-2, 2-3, 3-3
which is 3+2+1, 3 positions starting at 1, 2 positions starting at 2, 1 starting at 3.
"""
from collections import defaultdict
class Solution:
    def solve(self, nums):
        d=defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
        return sum(len(l)*(len(l)+1)//2 for l in d.values())
