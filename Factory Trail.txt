"""
Factory Trail

Fancy math explained here: https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
"""
class Solution:
    def solve(self, n):
        count = 0
        i=5
        while (n/i>=1): 
            count += int(n/i) 
            i *= 5
        return int(count) 