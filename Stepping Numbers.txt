"""
Stepping Numbers

DP solution: For each digit d, the number of ways of getting a number finishing by d of length n is the number of ways of getting a number of length n-1 finishing with d-1 or d+1.

So we start with the first digit, all ones except zero because our number cant have a leading 0. Then each n steps, we sum the diagonals, unless we are on the edge (0 or 9). 
"""
MOD=10**9 + 7
class Solution:
    def solve(self, n):
        if n == 1: return 10
        digits = [1 for _ in range(10)]
        digits[0]=0
        for _ in range(n-1):
            next_d = [0 for _ in range(10)]
            for i,v in enumerate(digits):
                if i>0: next_d[i-1] += v
                if i < len(next_d) - 1: next_d[i+1] += v
            digits=next_d
        return sum(digits)%MOD
