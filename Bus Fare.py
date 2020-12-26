"""
Bus Fare

DP + Binary Search:

We find the farthest position we can reach using binary search since dates are increasing. Then, we minimize the cost obtained from the different jumps we can make.
"""
from bisect import bisect_left
from functools import lru_cache
class Solution:
    def solve(self, days):
        @lru_cache(None)
        def dp(i=0):
            if i == len(days): return 0
            cur_day = days[i]
            j = bisect_left(days, cur_day+1)
            k = bisect_left(days, cur_day+7)
            l = bisect_left(days, cur_day+30)
            return min(dp(j)+2, dp(k)+7, dp(l)+25)
        return dp()
            
