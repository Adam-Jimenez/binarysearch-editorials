"""
3 and 7

Mutiples of three:
0,3,6,9,12,15,18,21,...

Mutiples of seven:
0,7,14,21,...

By removing 7 or 14, we fall back on a multiple of 21, which is also a multiple of 3.

In the general case ax+by = c where a,b,c are integers, check out linear diophantine equations:

https://brilliant.org/wiki/linear-diophantine-equations-one-equation/
"""
class Solution:
    def solve(self, n):
        return any((
            not n%3,
            n>=7 and not (n-7)%3,
            n>=14 and not (n-14)%3
        ))
