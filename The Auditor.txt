"""
The Auditor

This is a classic base conversion problem in disguise. We must go from base 26 to base 10, where every character's value is its position in the alphabet, 1-indexed.

Note: using a dictionary to store the characters values would be more efficient than index()
"""
from string import ascii_uppercase as alphabet
class Solution:
    def solve(self, s):
        ans=0
        for c in s:
            ans*=26
            ans+=alphabet.index(c)+1
        return ans