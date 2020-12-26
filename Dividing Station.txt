"""
Dividing Station

One key insight to this problem is that, if a number is divisible by the largest number of a subset, it will be divisible by all the other numbers, because the largest number is a multiple of them.

Following that logic, we can sort the numbers and for each number I check if it divisible by the largest number of the current subset and if so, I add it. If it doesn't belong to any existing subset, I create a new subset.
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        ss=[[nums.pop(0)]]
        for n in nums:
            found=False
            for subset in ss:
                if n%subset[-1]==0:
                    subset.append(n)
                    found=True
            if not found:
                ss.append([n])
        return max(len(x) for x in ss)
            
    