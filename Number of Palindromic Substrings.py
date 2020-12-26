"""
Number of Palindromic Substrings

We try every possible center for our palindromes, expanding as much as possible. This works because the center part of a palindrome is a palindrome as well:

tacocat
acoca
coc
o
"""
class Solution:
    def solve(self, s):
        def expand(i,j):
            ans=0
            while i>=0 and j<len(s) and s[i] == s[j]:
                i-=1
                j+=1
                ans+=1
            return ans
        return sum(expand(i,i)+expand(i,i+1) for i in range(len(s)))