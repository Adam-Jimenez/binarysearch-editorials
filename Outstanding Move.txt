"""
Outstanding Move

O(N^2) solution. We compute the result for the original order, then we iterate over each number. For each number, if we want to move it to a position, we add its value once per index moved, and we subtract each values met. If we move to the left, we subtract the value for each index and we add each number met.
"""
class Solution:
    def solve(self, nums):
        orig = compute(nums)
        off=0
        for i,n in enumerate(nums):
            cur=0
            for j in range(i+1, len(nums)):
                cur+=n
                cur-=nums[j]
                off=max(off,cur)
        for i,n in enumerate(nums):
            cur=0
            for j in range(i-1, -1, -1):
                cur-=n
                cur+=nums[j]
                off=max(off,cur)
        return orig+off
def compute(lst):
    return sum((i+1)*v for i,v in enumerate(lst))
