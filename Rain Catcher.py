"""
Rain Catcher

The volume in each square is constrained by the minimum between the highest wall to the left of the current square and the highest wall to the right of the current square. 
"""
class Solution:
    def solve(self, nums):
        l = [0 for _ in nums]
        r = [0 for _ in nums]
        for i in range(1,len(nums)):
            l[i] = max(l[i-1], nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            r[i] =  max(r[i+1], nums[i+1])
        return sum(max(0, min(l[i],r[i])-nums[i]) for i in range(len(nums)))
