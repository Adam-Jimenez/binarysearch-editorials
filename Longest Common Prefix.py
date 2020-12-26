"""
Longest Common Prefix

We can compare characters at the same position by zipping them together, and to check if they're all equal we can check that the set of characters is length 1.
"""
class Solution:
    def solve(self, words):
        ans=""
        for x in zip(*words):
            if len(set(x))==1:
                ans+=x[0]
            else: break
        return ans
