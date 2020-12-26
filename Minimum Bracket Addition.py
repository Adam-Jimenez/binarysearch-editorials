"""
Minimum Bracket Addition

When the bracket running count goes under 0, it means you are closing brackets that were never opened, so with certainty you will need to open it, so it adds one to the answer.

In the other case, you need to close the parentheses that were never closed at the end, so you add the running count.
"""
class Solution:
    def solve(self, s):
        cnt = ans = 0
        for c in s:
            cnt += ") (".index(c) - 1
            if cnt < 0:
                cnt=0
                ans+=1
        return ans+cnt