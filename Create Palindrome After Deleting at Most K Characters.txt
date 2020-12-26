"""
Create Palindrome After Deleting at Most K Characters

We can start from the center of a potential palindrome, and then each time we have equal characters, we return dp(i-1, j+1), and if we have non-equal characters we return min(dp(i-1,j), dp(i,j+1))+1 to simulate removing either the left or the right character. When we reach the edge of the string we have to remove all the remaining characters on the other side.
"""
from functools import lru_cache
class Solution:
    def solve(self, s, k):
        @lru_cache(None)
        def dp(i,j):
            if i<0 and j>=len(s):
                return 0
            if i<0:
                return len(s)-j
            if j>=len(s):
                return i+1
            if s[i]==s[j]:
                return dp(i-1, j+1)
            else:
                return min(dp(i-1, j), dp(i,j+1))+1
        return any(dp(i,i)<=k or dp(i,i+1)<=k for i in range(len(s)))
