"""
Non-Decreasing Digits

Imagine a 2 digit number: 43. If it doesn't satisfy the conditions, we subtract one to the left number and set the second one to 9, because 9 will always respect the constraint and it is the closest number going down.

When we have a longer number: 123123, and we find a decreasing pair of digits (3,1), we can repeat the process and get: 122923. But now we have the same problem with (9,2). Notice how we skipped 122999 by subtracting to the original number. In fact, we can always set everything to 9 from the leftmost number where the non-decreasing constraint is not respected, so we can find the leftmost digit that break the constraint and set everything to its right to 9, and then subtract one from it.
"""
class Solution:
    def solve(self, n):
        digits=[int(x) for x in str(n)]
        left_bound=None
        for i in range(len(digits)-1,0,-1):
            if digits[i]<digits[i-1]:
                left_bound=i
                digits[i-1]-=1
        if left_bound:
            for i in range(left_bound, len(digits)):
                digits[i]=9
        return int("".join(map(str,digits)))