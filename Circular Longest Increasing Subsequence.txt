"""
Circular Longest Increasing Subsequence

We can use the O(n log n) approach to finding the longest increasing subsequence on an "unwrapped" array made by duplicating the original array. If you don't know the O(n log n) way to finding the LIS, look at the simpler version of this problem - longest increasing subsequence.
"""
from bisect import bisect_left
class Solution:
    def solve(self, nums):
        a=nums+nums
        ans=0
        for i in range(len(nums)):
            dp=[]
            for j in range(i, len(nums)+i):
                n=a[j]
                k=bisect_left(dp,n)
                if k==len(dp):
                    dp.append(n)
                else:
                    dp[k]=n
            ans=max(ans,len(dp))
        return ans
