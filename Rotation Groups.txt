"""
Rotation Groups

For every word we meet, we increment our answer if its not in our set.
We then generate all rotations of the word and store them in our set.
"""
class Solution:
    def solve(self, words):
        s=set()
        ans=0
        for w in words:
            if w not in s: ans+=1
            for i in range(len(w)):
                s.add(w[i:] + w[:i])
        return ans
