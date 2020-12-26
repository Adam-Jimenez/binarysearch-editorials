"""
Factorial Sum

For each factorial f(i), f(i) is greater than the sum of f(1)+f(2)+...+f(i-1). That is because we multiply the greatest value of the sequence by i, one times more than the number of elements in the previous sequence. 

Therefore, we know if f(i) is smaller than n, we have to use it in our sum of factorials, because if we don't we will never get a value big enough to reach n. 

So we iterate from an arbitrary upper bound (20 in this case) and descend, removing each value big enough to fit in n, and check if we reach 0.
"""
from math import factorial as f
class Solution:
    def solve(self, n):
        for i in range(20,0,-1):
            fact=f(i)
            if fact<=n:
                n-=fact
        return n==0
