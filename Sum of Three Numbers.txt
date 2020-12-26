"""
Sum of Three Numbers

To pick the first number, we iterate over the list.
To pick the next two, we put a pointer after i, and one to the end of the list. 

Because we sorted, we know every value after j will be greater than it, and every value before k will be smaller. So if our sum isn't big enough, we can increment j to get the next biggest value. If it's too big, we can decrement k.
"""
class Solution:
    def solve(self, nums, k):
        nums.sort()
        for i in range(len(nums)-2):
            target=k-nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k] < target: j+=1
                elif nums[j]+nums[k] > target: k-=1
                else: return True
        return False
