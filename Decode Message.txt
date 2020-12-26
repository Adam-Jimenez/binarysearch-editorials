"""
Decode Message

Recursive solution with memoization. The number of ways to decode the string from index i is the number of ways to decode the string from index i+1 and i+2, if the next two digits fit in the [1,26] range.
"""
from functools import lru_cache
class Solution:
    def solve(self, message):
        @lru_cache(None)
        def dp(i):
            if i>=len(message): return 1
            ans = dp(i+1)
            if i<len(message)-1 and 1<=int(message[i:i+2])<=26:
                ans+=dp(i+2)
            return ans
        return dp(0)
