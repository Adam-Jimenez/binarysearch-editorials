"""
Switcheroo

For a switch to be one, it must have a odd number of divisor, because each divisor will flip the switch. 

The only numbers with this property are perfect squares, because normally each number has an even number of divisors, making up pairs. take 14 (not a perfect square):
1 14
2 7
But when we have a perfect square (ex: 16):
1 16
2 8
4 4
One divisor will be repeated within a pair, making the total number of unique divisors odd. 

Taking the square root of a number will give the number of perfect squares, because every square in range [1,n] is in range [1, n^2] and we reverse this mapping.
"""
from math import sqrt
class Solution:
    def solve(self, n):
        return int(sqrt(n))
