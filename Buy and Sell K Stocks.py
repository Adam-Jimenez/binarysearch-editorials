"""
Buy and Sell K Stocks

Top-down DP solution: 

For each index in the array, we have two possibilites: either buy/sell the stock (depending if we are holding one currently) or do nothing. So we take the max of the two options.
"""
from functools import lru_cache
class Solution:
    def solve(self, prices, k):
        @lru_cache(None)
        def dp(i, k, bought):
            if i==len(prices) or k==0: return 0
            if bought:
                return max(dp(i+1, k-1, False)+prices[i], dp(i+1,k,bought))
            else:
                return max(dp(i+1,k,True)-prices[i], dp(i+1,k,bought))
        return dp(0,k,False)
