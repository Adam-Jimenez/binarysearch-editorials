"""
Longest Alternating Subsequence

We can keep two dp arrays - one where the last number is increasing and one where the last number is decreasing. 
"""
class Solution:
    def solve(self, nums):
        if not nums: return 0
        inc=[1 for _ in nums]
        dec=[1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], dec[j]+1)
                elif nums[i] < nums[j]:
                    dec[i] = max(dec[i], inc[j]+1)
        return max(max(inc),max(dec))