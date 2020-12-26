"""
Zipped String

We can use DP where i in the position in a, j the position in b and k the position in c.

Whenever a[i] == c[k], we can test dp(i+1,j,k+1)
Whenever b[j] == c[k], we can test dp(i, j+1, k+1)

If we reach the end of each string, we return True.
"""
from functools import lru_cache
class Solution:
    def solve(self, a, b, c):
        @lru_cache(None)
        def dp(i=0,j=0,k=0):
            if i == len(a) and j == len(b) and k == len(c): return True
            if k == len(c): return False
            if i<len(a) and a[i] == c[k] and dp(i+1,j,k+1): return True
            if j<len(b) and b[j] == c[k] and dp(i, j+1, k+1): return True
            return False
        return dp()