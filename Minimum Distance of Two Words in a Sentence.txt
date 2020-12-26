"""
Minimum Distance of Two Words in a Sentence

Remember when you last saw word0 and word1, and check the distance with the last word0 when you see word1 and word1 when you see word0.
"""
from itertools import groupby
class Solution:
    def solve(self, text, word0, word1):
        if word0 not in text or word1 not in text: return -1
        last0=-1e9
        last1=-1e9
        ans=1e9
        for i,w in enumerate(text.split()):
            if w == word0:
                ans=min(ans, i-last1-1)
                last0=i
            if w == word1:
                ans=min(ans, i-last0-1)
                last1=i
        return ans