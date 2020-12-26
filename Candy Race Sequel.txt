"""
Candy Race Sequel

Top-down dynamic programming solution:

We try each possible move, taking 1,2 or 3 candy, and subtract the optimal answer for the subproblem starting after our move. 
Since the subproblem starting after our move is the subproblem where Lawrence is starting, each points he makes reduces our score. 

To be winning, we need a greater score than lawrence, and since we subtract lawrence's score, we can check if we have a relative score greater than zero.

O(n) time
O(n) space
"""
from functools import lru_cache
class Solution:
    def solve(self, nums):
        @lru_cache(None)
        def dp(i=0):
            if i >= len(nums): return 0
            return max(
                nums[i]-dp(i+1),
                nums[i]+nums[i+1]-dp(i+2) if i < len(nums)-1 else 0,
                nums[i]+nums[i+1]+nums[i+2]-dp(i+3) if i < len(nums)-2 else 0,
            )
        return dp()>0
