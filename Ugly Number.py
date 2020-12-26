"""
Ugly Number

We remove all 2,3,5 factors from the number. If there is anything left, it means there are greater prime factors left to be explored.
"""
class Solution:
    def solve(self, n):
        for d in (2,3,5):
            while n%d==0:n=n//d
        return n==1
        
