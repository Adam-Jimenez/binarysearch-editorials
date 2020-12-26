"""
Fleet of Palindromes

We can spread characters with even frequencies amongst our palindromes as we wish, but we can only have one uneven frequency character per palindrome, so we check if there is less or equal than k uneven frequency. We also assume that len(s) >= k.
"""
from collections import Counter
class Solution:
    def solve(self, s, k):
        return sum(1 for k,v in Counter(s).items() if v&1) <= k
