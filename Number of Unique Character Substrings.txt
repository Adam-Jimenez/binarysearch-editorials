"""
Number of Unique Character Substrings

For a substring of repeating characters e.g. "aaaa", where n = len(s), we will have:
1 substring of length 4 : "aaaa"
2 substrings of length 3: "aaa", "aaa"
3 substrings of length 2: "aa", "aa", "aa"
4 substrings of length 1: "a", "a", "a", "a"

So the number of substrings will be 1+2+...+n, which is a known arithmetic sequence that equals n*(n+1)/2.
"""
from itertools import groupby
class Solution:
    def solve(self, s):
        ans=0
        for _, grp in groupby(s):
            n=len(list(grp))
            ans+=n*(n+1)//2
        return ans
