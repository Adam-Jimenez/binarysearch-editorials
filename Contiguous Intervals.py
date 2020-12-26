"""
Contiguous Intervals

We iterate over the sorted numbers, each time the present number isn't equal to the past number, we append the interval. 

Trick so you don't have to deal with edge cases: add big value at end, so you don't need to check if you reached the end, or if the list is at least length 2.
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        nums.append(1e9)
        ans=[]
        l=nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                ans.append([l, nums[i-1]])
                l=nums[i]
        return ans