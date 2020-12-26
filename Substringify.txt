"""
Substringify

We try every possible offset for the substring t, and then we compute the cost of making it equal to the substring of s by checking the number of unequal characters.
"""
class Solution:
    def solve(self, s, t):
        ans=len(t)
        for i in range(len(s)-len(t)+1):
            a=len(t)
            for j in range(len(t)):
                if t[j] == s[i+j]: a-=1
            ans=min(ans, a)
        return ans