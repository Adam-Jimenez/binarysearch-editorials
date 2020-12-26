"""
Reverse Sublists to Convert to Target

If we can reverse any sublist, it means we can swap any two elements. For example: [1,2,3,4,5]. If we want to swap 1 and 5, we must reverse the whole array, then reverse the array between 1 and 5:
[5,4,3,2,1]
[5,2,3,4,1]
If we can swap any arbitrary elements, we can reorder the array as we wish, so the only constraint for this problem is that nums and target contain the same values.

Seen here: https://leetcode.com/contest/biweekly-contest-27/problems/make-two-arrays-equal-by-reversing-sub-arrays/
"""
from collections import Counter
class Solution:
    def solve(self, nums, target):
        return Counter(nums) == Counter(target)
