"""
Dominos

Similar to Tromino Theory;

 We have two different states with different recurrence relations: The state where the board is flat and the state where there is a hole on the sides. We count the different states we can reach from each of them. 

Explained in this video I made: https://www.youtube.com/watch?v=ccbPq-CqVRk
"""
from functools import lru_cache
MOD = (10**9) + 7
class Solution:
    def solve(self, n):
        @lru_cache(None)
        def f(n):
            if n == 0: return 1
            if n < 0: return 0
            return (f(n-2) + 2*f(n-2) + 2*g(n-2)) % MOD
            
        @lru_cache(None)
        def g(n):
            if n <= 0: return 0
            return (f(n-2) + g(n-2)) % MOD
            
        return f(n)
