"""
Repeating String

For all cycle lengths, we check if the start of the string repeated equals the original string. We only need to check up to the half of the string, and only if the cycle length is a divisor of the length of the string.
"""
from itertools import cycle
class Solution:
    def solve(self, s):
        return any(all(x==y for x,y in zip(s,cycle(s[:i]))) for i in range(1,1+len(s)//2) if len(s)%i==0)
            
