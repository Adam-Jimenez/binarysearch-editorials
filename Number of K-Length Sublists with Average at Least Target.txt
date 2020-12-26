"""
Number of K-Length Sublists with Average at Least Target

Knowing that the sublist will always be of length k, if we multiply the target by k, we can solve for the sum instead of the average, since the average is the sum divided by the number of elements.

So, we apply a sliding-window sum, and check if the sum respects the constraint and increment our answer.

O(n) time, O(1) space
"""
class Solution:
    def solve(self, nums, k, target):
        target*=k
        sum=0
        ans=0
        for i,n in enumerate(nums):
            if i>=k:
                sum-=nums[i-k]
            sum+=n
            if i>=(k-1):
                if sum>=target:
                    ans+=1
        return ans