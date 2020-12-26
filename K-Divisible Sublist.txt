"""
K-Divisible Sublist

The sum of a sublist [i:j] can be defined as the prefix sum ending at j minus the prefix sum ending at i.

If we want the sum to be a multiple of k, the sum modulo k must equal 0. 

If the prefix sum modulo k ending at j is equal to the prefix sum modulo k ending at i, it means the sum in between modulo k is equal to 0, so it is a multiple of k.

Thanks to xiao for the insight.
"""
class Solution:
    def solve(self, nums, k):
        pre=[nums[0]%k]
        for i in range(1,len(nums)):
            pre.append((pre[-1]+nums[i])%k)
        s=set([0])
        for i in range(1,len(nums)):
            if pre[i] in s: 
                return True
            s.add(pre[i-1])
        return False
