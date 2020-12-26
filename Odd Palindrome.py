"""
Odd Palindrome

Every even-length palindrome is composed of two consecutive equal character at its center.
"""
class Solution:
    def solve(self, s):
        for i in range(1,len(s)):
            if s[i] == s[i-1]:return False
        return True
