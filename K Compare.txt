"""
K Compare

We find the kth largest number in b. If a number if smaller than the kth largest number, it will be smaller than larger numbers as well. So we return the number of numbers in a that are smaller than that target number.
"""
class Solution:
    def solve(self, a, b, k):
        if k>len(b): return 0
        if k==0: return len(a)
        b.sort()
        return sum(1 for n in a if n<b[-k])
