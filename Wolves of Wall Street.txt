"""
Wolves of Wall Street

We buy and sell the next day, and if the result was negative we just pretend nothing happened :) don't try this at home
"""
class Solution:
    def solve(self, prices):
        return sum(max(0,prices[i]-prices[i-1]) for i in range(1,len(prices)))
