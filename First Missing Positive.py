"""
First Missing Positive

O(n) time, O(n) space solution.

Create a set from all numbers. Start from one, and increment each time you find the value in the set. 

O(1) space is possible:
https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
"""
class Solution:
    def solve(self, nums):
        s=set(nums)
        i=1
        while i in s:
            i+=1
        return i
