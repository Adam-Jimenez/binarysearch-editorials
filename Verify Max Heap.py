"""
Verify Max Heap

We can simply check the rules specified in the problem statement.
"""
class Solution:
    def solve(self, nums):
        for i in range(len(nums)//2):
            for j in range(1,3):
                if 2*i+j >= len(nums): break
                if nums[i]<nums[2*i+j]: return False
        return True