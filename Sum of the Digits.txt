"""
Sum of the Digits

We take the last digit by computing modulo ten, and then we shift the number to the right by dividing by ten. The divmod function can do both of those operation at the same time.
"""
class Solution:
    def solve(self, num):
        a=0
        while num:
            num,m=divmod(num,10)
            a+=m
        return a
