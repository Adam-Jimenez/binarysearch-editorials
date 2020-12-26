"""
Kth Missing Number

Since the array is sorted, we can compare adjacent element to find the number of number missing in between them:

nums[i]-nums[i-1]-1 will give us the count of missing numbers in between the two numbers.

If the number of missing numbers in between two indices is smaller than k, we know that the kth missing number isn't between those two indices, so we remove the difference from k and move on.

Otherwise, we can get the kth missing numbers by counting the offset from the first possible missing numbers, nums[i-1]+1+k.

O(n) time, O(1) space. 

Edit: I think this can be done in O(log n) time.
"""
class Solution:
    def solve(self, nums, k):
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]-1
            if k >= diff:
                k-=diff
            else:
                return nums[i-1]+k+1
        return nums[-1]+k+1
