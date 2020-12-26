"""
Longest Increasing Subsequence

O(n log n) approach: https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

We keep an array (dp), where dp[i] represents the last value of the longest increasing subsequence of size (i+1). If our current value (n) is greater than the last value, we can make a longer subsequence by appending n to our dp array. Since it has to respect the LIS rules, our dp array will be strictly increasing, so we can binary search on it to find the position of the current n. 
"""
from bisect import bisect_left
class Solution:
    def solve(self, nums):
        dp=[]
        for n in nums:
            i=bisect_left(dp, n)
            if i==len(dp):
                dp.append(n)
            else:
                dp[i]=n
        return len(dp)
