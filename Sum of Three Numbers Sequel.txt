"""
Sum of Three Numbers Sequel

O(n^2) solution.

We sort the number, so we know what to do when we are smaller or bigger than the target.

When we are smaller, we know we have to increment one of the numbers, otherwise we need to reduce one of our numbers.

That is the logic behind this algo: Select one number, and then use two pointers for the next two numbers: the smallest value and the greatest value after i. Compute the sum, and if we are greater than target, reduce greatest value and if smaller, increment smaller number.
"""
class Solution:
    def solve(self, nums, target):
        nums.sort()
        ans=1e9
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s<=target:
                    ans=min(ans,target-s)
                    j+=1
                else:
                    ans=min(ans,s-target)
                    k-=1
        return ans
