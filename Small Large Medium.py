"""
Small Large Medium

https://leetcode.com/problems/132-pattern/submissions/
"""
class Solution:
    def solve(self, nums):
        mins=[1e9 for _ in nums]
        for i,n in enumerate(nums):
            mins[i]=n
            if i > 0 and mins[i-1]<mins[i]: mins[i]=mins[i-1]
        stk=[]
        for i in range(len(nums)-1,-1,-1):
            while stk and stk[-1] <= mins[i]: stk.pop()
            if stk and stk[-1]<nums[i]: return True
            stk.append(nums[i])
        return False