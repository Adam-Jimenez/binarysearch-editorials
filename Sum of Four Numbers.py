"""
Sum of Four Numbers

Recursive general solution, that applies to an arbitrary amount of numbers. We recursively iterate through every number, either picking it or not. When we reach a leaf, we check if we reached the target sum and count.
"""
class Solution:
    def solve(self, nums, k):
        def dp(i,rem,cnt):
            if rem==0 and cnt==0: return True
            if i==len(nums) or rem<0 or cnt==0: return False
            return dp(i+1,rem,cnt) or dp(i+1, rem-nums[i], cnt-1)
        return dp(0,k,4)