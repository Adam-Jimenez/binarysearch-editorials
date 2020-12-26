"""
K Prefix

We can simply compute the prefix sum for each i, then iterate from the right until we find a position that satisfies the constraint.
"""
class Solution:
    def solve(self, nums, k):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=k: return i
        return -1