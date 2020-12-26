"""
Tromino Theory

Top-down version of lawrence's editorial :)           
"""
from functools import lru_cache
MOD=10**9 + 7
class Solution:
    def solve(self, n):
        @lru_cache(None)
        def f(n):
            if n <= 2: return n
            return (f(n-1) + f(n-2) + 2*g(n-2)) % MOD
        @lru_cache(None)
        def g(n):
            if n <= 2: return n
            return (f(n-1) + g(n-1)) % MOD
        return f(n)