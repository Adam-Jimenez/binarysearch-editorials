"""
Wolf of Wall Street

Buy high sell low.

The best time to buy a stock was at its lowest point in the past, and the best moment to sell is at the maximum point from the lowest.
"""
class Solution:
    def solve(self, prices):
        mx=0
        m=prices[0]
        for p in prices:
            m=min(m,p)
            mx = max(mx, p-m)
        return mx
