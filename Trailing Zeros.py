"""
Trailing Zeros

The key insight to the types of problem asking for the trailing number of zeroes is the following.

The number of trailing zeroes is the number of times 10 can divide a number. The number of tens in a number can be found by doing its prime factorization: each ten is composed of prime factors 2 and 5, so the number of pairs of 2 and 5 in the prime factors of a number will give the number of trailing zeroes.

Now, we must find the smallest value that can be divided by numbers [1,k], otherwise known as the least common multiple (lcm). Let's take an example (k=5):
lcm(1,2,3,4,5) = lcm(1,lcm(2,lcm(3,lcm(4,5))))
lcm(4,5) =20
lcm(3,20)=60
lcm(2,60)=60
lcm(1,60)=60 
A key insight here is that lcm(2,4) = 4, so we can ignore the 2 completely. The reason for this is that 4 is a multiple of 2.
lcm(1,3,4,5)=1x3x4x5=60 (No number is a multiple of another).

How does this help us counting the number of 10's? Well, if we can eliminate numbers for which one of their multiples is present in the series, it means if we have 5,10,15,20, we can eliminate 5,10,15 and just keep the largest number (20), and its prime factors are 2x2x5. In order to gain another 5, we must reach the next power of 5, 25:

25 = 5*5. => k=25 will have two trailing zeroes because we have two 5's. 
We can assume there will be enough 2's in the series because 2 is more frequent than 5, (2,4,6,8,...) vs (5,10,15,...)

Hopefully this gives you the intuition (smiley face).
"""
from math import log
class Solution:
    def solve(self, k):
        return int(log(k,5))
