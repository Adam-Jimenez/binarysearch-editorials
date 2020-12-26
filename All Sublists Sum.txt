"""
All Sublists Sum

Any contiguous subarray can be defined by their left bound and their right bound: i,j.

For a position k to be contained within a subarray, i <= k <= j.
The number of possibilities for i that satisfy this condition are k+1 and the number of possibilities for j is N-k.

We can get the number of combinaison by doing the product of possibilities, which results in the number of occurences of the number.
"""
class Solution:
    def solve(self, nums):
        N=len(nums)
        ans=0
        for i in range(len(nums)):
            n=nums[i]
            ans += (i+1) * (N-i) * n
        return ans%1000000007
