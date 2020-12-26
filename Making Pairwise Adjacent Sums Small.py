"""
Making Pairwise Adjacent Sums Small

We iterate over the array, reducing the 2nd element from the pair as much as needed, and doing so will minimize the subtraction needed for the next pair including it. 

We make sure that we don't go under zero because the operation only applies to positive values.

O(n) time, O(1) space
"""
MOD=10**9 + 7
class Solution:
    def solve(self, nums, k):
        ans=0
        for i in range(0,len(nums)-1):
            sm = nums[i]+nums[i+1]
            diff=max(sm-k,0)
            nums[i+1]-=diff
            if nums[i+1]<0:
                nums[i+1]=0
            ans+=diff
        return ans % MOD
