"""
Number of Unique Binary Search Trees

The unique numbers of valid BSTs follow the Catalan sequence.

Why? I don't know. I let the smart people do the math.

https://en.wikipedia.org/wiki/Catalan_number
"""
from math import factorial as f
class Solution:
    def solve(self, n):
        return f(2*n)//(f(n+1)*f(n)) % (10**9+7)
