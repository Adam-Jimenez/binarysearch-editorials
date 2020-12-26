"""
Bear of Wall Street

Classic DP problem solved with Top-down approach for simplicity.

For each price point:
- if we're holding a stock we try doing nothing and skipping the current day, or selling and waiting one day.
- If we're not holding a stock, we try doing nothing and skipping the current day, or buying at the current price.

Video explanation: https://www.youtube.com/watch?v=upsJfSAE968
"""
from functools import lru_cache
class Solution:
    def solve(self, prices):
        @lru_cache(None)
        def dp(i=0, holding=False):
            if i >= len(prices): return 0
            if not holding:
                return max(dp(i+1, holding), dp(i+1,True)-prices[i])
            if holding:
                return max(dp(i+1, holding), dp(i+2,False)+prices[i])
        return dp()
                