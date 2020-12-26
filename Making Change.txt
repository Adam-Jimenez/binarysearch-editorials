"""
Making Change

In this specific situation, we can greedily pick the maximal number of the largest coin possible. This wouldn't work if we had coins of value (4,3,1) and n=6, for example.

This paper explains how to figure out when greedy is possible: https://graal.ens-lyon.fr/~abenoit/algo09/coins2.pdf
Warning: contains math
"""
class Solution:
    def solve(self, n):
        ans=0
        for change in [25,10,5,1]:
           times,n = divmod(n,change)
           ans+=times
        return ans
