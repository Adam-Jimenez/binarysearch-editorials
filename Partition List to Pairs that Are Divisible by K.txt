"""
Partition List to Pairs that Are Divisible by K

We count all numbers modulo k. Let's say a number has a remainder of 2 (mod 5), well it has to be matched to a number that has a remainder of 3 (mod 5) to complete the 5. So, each remainder must be equal to its complement (mod k), except when the remainder is 0 or half of k, then it matches with itself so it must be divisible by 2.

O(n) time, O(n) space
"""
from collections import Counter
class Solution:
    def solve(self, nums, k):
        c=Counter()
        for n in nums:
            c[n%k]+=1
        for n,v in c.items():
            if n == 0 or n == k/2:
                if v&1: 
                    return False
            else:
                if c[-n%k]!=v: 
                    return False
        return True
