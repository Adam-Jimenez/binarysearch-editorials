"""
Increasing Digits

Simple recursive solution for the non-math people like me. We iterate over all digits, and keep track of the previous digit and recurse when the current digit is greater. When we reach n == 0 we have a valid solution so we return 1.
"""
class Solution:
    def solve(self, n, prev=0):
        if n == 0: return 1
        ans=sum(self.solve(n-1,i) for i in range(1,10) if i>prev)
        return ans
