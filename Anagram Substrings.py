"""
Anagram Substrings

Sliding window using Counters. We count the frequency of characters in a window of size l (length of s0). If it equals the frequency of characters in s0, we have a permutation. Then we slide the window by incrementing by the following character frequency, and subtract the frequency of the character no longer included in the window.
"""
from collections import Counter
class Solution:
    def solve(self, s0, s1):
        l=len(s0)
        if l>len(s1): return 0
        c1=Counter(s0)
        c2=Counter()
        for i in range(l):
            c2[s1[i]]+=1
        ans=0
        for i in range(l, len(s1)):
            if c1==c2: ans+=1
            c2[s1[i-l]]-=1
            if c2[s1[i-l]] == 0: del c2[s1[i-l]]
            c2[s1[i]]+=1
        if c1==c2: ans+=1
        return ans
