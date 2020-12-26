"""
Robinhood

While the dollar amount is less than the target, apply one interest rate, then the other.
"""
class Solution:
    def solve(self, n, e, o, t):
        ans=0
        while n<t:
            n*=1+(e/100)
            ans+=1
            if n<t:
                n*=1+(o/100)
                ans+=1
        return ans
