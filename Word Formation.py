"""
Word Formation

If letters has every letter in the word (or more), it means that the intersection of the letters in word and letters will contain all the letters in word. 

I sorted by length so the first correct result we meet is the largest one, but it is more efficient to keep a max result.
"""
from collections import Counter
class Solution:
    def solve(self, words, letters):
        cl=Counter(letters)
        for w in sorted(words, key=len, reverse=True):
            cw=Counter(w)
            if cw&cl==cw:
                return len(w)
        return 0
