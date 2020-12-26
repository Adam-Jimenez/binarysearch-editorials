"""
Narcissistic Number

Use generator expressions to save space! Use strings to iterate over digits and do magic.
"""
class Solution:
    def solve(self, n):
        s=str(n)
        return n==sum(int(x)**len(s) for x in s)
