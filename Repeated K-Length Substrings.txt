"""
Repeated K-Length Substrings

One-line version of ruby's answer - we can sum the booleans directly so if they are true, they are equal to one.

Otherwise the logic is the same, we use a counter to count the frequencies of each k-length substring.

Time complexity: O(n*k), because slicing takes k steps and we repeat it up to n times
Space complexity: O(n*k), because we will store n substrings of length k
"""
from collections import Counter
class Solution:
    def solve(self, s, k):
        return sum(v>1 for v in Counter(s[i:i+k] for i in range(len(s)-k+1)).values())
