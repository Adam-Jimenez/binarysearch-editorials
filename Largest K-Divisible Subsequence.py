"""
Largest K-Divisible Subsequence

The constraints k is less than 10 gives us a hint about the state we need to track in our DP. In fact, we only need to know the current modulo in regards to k to know if our answer is valid, so when we pick a number, we update the (sum % k) and when we skip one number we leave it intact.

A neat trick is to return float('-inf') when an answer is invalid, as all the sums will be reduced to nothing.

Complexity is O(n*k), but since we know k is smaller than 10, this is practically linear.
"""
from functools import lru_cache
class Solution:
    def solve(self, nums, k):
        @lru_cache(None)
        def dp(i,sum_mod_k):
            if i == len(nums):
                if sum_mod_k == 0: 
                    return 0
                else:
                    return float('-inf')
            new_mod_k = (sum_mod_k + nums[i]) % k
            return max(dp(i+1, sum_mod_k), dp(i+1, new_mod_k)+nums[i])
        return dp(0, 0)
            
