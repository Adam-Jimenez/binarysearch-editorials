"""
K Maximum Non-Overlapping Sums

Top-down DP solution: for each index we have the choice between:
1. Starting a new sublist, adding our current number nums[i] to the total sum,
2. Continuing the current sublist, if we are in one (indicating by in_group),
3. Skipping the current number, ending the sublist if there was one.

Each time we start a sublist, we decrease the k remaining sublist left to create. When we finish the kth group - we return 0 to mark that we finished our sum, and if we reach an invalid state we return -infinity so it doesn't get picked when we maximize the results.
"""
from functools import lru_cache
class Solution:
    def solve(self, nums, k):
        @lru_cache(None)
        def dp(i, k,in_group=False):
            if k == 0 and (not in_group or i >= len(nums)): return 0
            if i>=len(nums) or k<0: return -1e9
            return max(
                nums[i] + dp(i+1,k - (not in_group), True),
                nums[i] + dp(i+1,k - 1, True),
                dp(i+1, k, False)
            )
        return dp(0,k)
            
                
