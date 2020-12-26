"""
Palindrome Count

We cut the string and half, and compute the number of possibilities by raising the number of letters to the number of characters used in the first half of the palindrome.
"""
class Solution:
    def solve(self, s, k):
        d,m = divmod(k,2)
        l=len(s)
        return l**d * l**m
