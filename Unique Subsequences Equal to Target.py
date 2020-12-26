"""
Unique Subsequences Equal to Target

DP O(n^2) solution: we can either skip the current character in s, or if it matches the current character in t, advance both pointers.
"""
from functools import lru_cache
MOD = 10**9 + 7
class Solution:
    def solve(self, s, t):
        if not t: return 0
        @lru_cache(None)
        def dp(i,j):
            if j == len(t): return 1
            if i == len(s): return 0
            ans=dp(i+1,j)
            if s[i] == t[j]:
                ans += dp(i+1, j+1)
            return ans % MOD
        return dp(0,0)
