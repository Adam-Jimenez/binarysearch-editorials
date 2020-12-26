"""
K and -K

We can use set comprehensions to build the set directly as well.
"""
class Solution:
    def solve(self, nums):
        x={n for n in nums if n>=0}
        y={-n for n in nums if n<=0}
        z=x&y
        return max(z) if z else -1
