"""
Word Concatenation

We store every word in a set for constant time lookup. Then, to find out if a word is a concatenation, we try cutting the string in half at every position, giving us a prefix and a suffix. If both the prefix and the suffix are in the set of words, or if they are a concatenation of words, the current word is a concatenation. We memoize the recursive function to avoid recomputation for the same words, and overlapping substrings.

`$O(n\times m^2)$` time (n words, m iterations per word with cost of m because of slicing)
`$O(n\times m)$` space
"""
from functools import lru_cache
class Solution:
    def solve(self, words):
        seen=set(words)
        @lru_cache(None)
        def is_concat(word):
            for i in range(1,len(word)):
                left=word[:i]
                right=word[i:]
                if all(ss in seen or is_concat(ss) for ss in (left,right)):
                    return True
            return False
        return sum(is_concat(w) for w in words)
            
