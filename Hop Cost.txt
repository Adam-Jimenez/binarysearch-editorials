"""
Hop Cost

From any starting position, we consider all the possible sub problems we can reach, we can either jump [1,dist], or switch lists and jump [1, dist]. We can do dynamic programming because there are overlapping subproblems; for example, we reach the same problem by jumping 1 step twice and making a 2-step jump once.

The base case is when we reach the end of a list, then we just return the value attained.

O(N^2), because there are 2xN unique states to our problem, and for each state we do 2xN calculations.
"""
from functools import lru_cache
class Solution:
    def solve(self, nums0, nums1, dist, cost):
        lists=[nums0,nums1]
        @lru_cache(None)
        def dp(i=0, cur_list=0):
            if i == len(nums0)-1: return lists[cur_list][i]
            ans=float('inf')
            for j in range(1,dist+1):
                k=i+j
                if k == len(nums0): break
                ans=min(ans, dp(k, cur_list)+lists[cur_list][i])
                ans=min(ans, dp(k, cur_list^1)+lists[cur_list][i]+cost) # switch
            return ans
        a= min(dp(0,0),dp(0,1))
        return a
