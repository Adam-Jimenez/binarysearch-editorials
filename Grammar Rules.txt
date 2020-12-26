"""
Grammar Rules

Since the permitted characters are constrained by the last picked character, we can define a lookup table giving us the allowed characters in function of the last picked character.

Then, we can iterate over the valid characters, and count the number of ways to solve the sub problem with n-1 and setting the last picked character with the current one.

The base case is when we reach an empty string - we have constructed a valid string according to the constraints.
"""
from functools import lru_cache
MOD=10**9+7
class Solution:
    def solve(self, n):
        if n == 0: return 0
        # Write your code here
        # a -> e
        # e -> a|i
        # i -> !i
        # o -> i|u
        # u -> a
        table = {
            "a": "e",
            "e": "ai",
            "i": "aeou",
            "o": "iu",
            "u": "a",
            None: "aeoui"
        }
        @lru_cache(None)
        def dp(n, last=None):
            if n == 0: return 1
            ans=0
            for c in table[last]:
                ans+=dp(n-1,c)
            return ans% MOD
        return dp(n)
    