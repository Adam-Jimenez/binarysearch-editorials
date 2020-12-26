"""
Break String Into Words

We convert the words into a set to be able to do constant time lookup. 

Then we start from the start of the string, iterating over the string and storing the characters.
If we match a word in the set, we recursively retry accumulating from that point on and if it doesn't work we keep accumulating till the end of the word. If we exhaust our options there is no solution.

lru_cache ensures we don't recompute the outcomes for the same value of i, reducing this problem to O(n^2)
"""
from functools import lru_cache
class Solution:
    def solve(self, words, s):
        words=set(words)
        @lru_cache(None)
        def rec(i=0):
            if i == len(s): return True
            acc=""
            for j in range(i, len(s)):
                acc+=s[j]
                if acc in words:
                    if rec(j+1): return True
            return False
        return rec()
