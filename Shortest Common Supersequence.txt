"""
Shortest Common Supersequence

This problem can be solved using longest common subsequence:

With:
a = "bell"
b = "yellow"
"ell" is the longest common subsequence, so if we concatenate both strings:
"bellyellow", we can remove the lcs to get "byellow".
"""
from functools import lru_cache
class Solution:
    def solve(self, a, b):
        @lru_cache(None)
        def lcs(i,j):
            if i==len(a) or j == len(b): return 0
            if a[i]==b[j]:
                return 1 + lcs(i+1,j+1)
            return max(lcs(i+1,j), lcs(i,j+1))
        return len(a)+len(b)-lcs(0,0)
