"""
Planar Edges

I literally just browsed this wikipedia page (https://en.wikipedia.org/wiki/Catalan_number) and I saw a familiar problem on the right...
"""
from math import comb
class Solution:
    def solve(self, n):
        if n&1: return 0
        n //= 2
        return comb(2*n, n) // (n+1) % (10 ** 9 + 7)