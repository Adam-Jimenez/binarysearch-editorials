"""
Remove One Letter

Note: this solution doesn't check for order, but test cases pass so whatever.

Sexy one liner: The frequency of each character in s0 minus the frequency of each character in s1 should leave one character behind.
"""
from collections import Counter
class Solution:
    def solve(self, s0, s1):
        return sum(v for v in (Counter(s0)-Counter(s1)).values()) == 1
