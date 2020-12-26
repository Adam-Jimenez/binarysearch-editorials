"""
N Lexicographic Integers

We can use the key attribute of sort to specify a function to map the value before comparing.
"""
class Solution:
    def solve(self, n):
        return sorted(range(1,n+1), key=str)
