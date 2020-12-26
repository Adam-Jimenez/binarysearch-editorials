"""
Trimmed Palindromes

This problem is exactly the same as the number of substring palindrome, because substrings are made from trimming left and right.
"""
class Solution:
    def solve(self, s):
        c=0
        for i in range(len(s)):
            c+=expand(i,i,s)
            c+=expand(i,i+1,s)
        return c

def expand(i,j,s):
    c=0
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
        c+=1
    return c