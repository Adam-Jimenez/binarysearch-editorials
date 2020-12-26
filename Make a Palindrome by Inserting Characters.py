"""
Make a Palindrome by Inserting Characters

For each non-matching character, we can either add an imaginary character to the left of the string to match the right one (in that case, we will only move j to the left) or add an imaginary character to the right of the string to match the left one (in that case, we will move i to the right). Since palindromes contain smaller palindromes, we can do this recursively. Example:

"radar" -> "ada" -> "d".

Here a letter is missing, so we just shift one pointer, which is equivalent to adding the correct character:

"rada"  -> "ada" -> "d".
"adar" -> "ada" -> "d".
"""
from functools import lru_cache
class Solution:
    def solve(self, s):
        @lru_cache(None)
        def dp(i,j):
            if i>=j: return 0
            if s[i]==s[j]:
                return dp(i+1,j-1)
            else:
                return min(dp(i+1,j), dp(i,j-1))+1
        return dp(0,len(s)-1)