"""
Making Change Sequel

M[i,k] = min(M[i-1,k], M[i,k-denominations[i]] + 1)

Since we copy the previous row of the 2D dp matrix, we can just reuse the same row
"""
from functools import lru_cache
class Solution:
    def solve(self, denominations, amount):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0]=0
        for d in denominations:
            for i in range(d, len(dp)):
                if dp[i-d] < dp[i]:
                    dp[i] = dp[i-d] + 1
        return dp[-1] if dp[-1] < float('inf') else -1
