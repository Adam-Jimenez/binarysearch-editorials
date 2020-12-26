"""
Two Lists' Median

Yeah sure, there's a fancy way of doing it. But this passes the test cases just fine. Maybe this is a lesson in over-engineering?
"""
class Solution:
    def solve(self, nums0, nums1):
        return median(sorted(nums0+nums1))

def median(a):
    return a[len(a)//2]