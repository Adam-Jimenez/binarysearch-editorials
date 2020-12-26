"""
Diminishing Words

We try all possible letter removal, and if its valid we repeat the process on the sub-word.
"""
class Solution:
    def solve(self, words, s):
        mx=0
        def dfs(w,depth=1):
            if w not in words: return
            nonlocal mx
            mx=max(mx,depth)
            for i in range(len(w)):
                w2 = w[:i] + w[i+1:]
                dfs(w2,depth+1)
        dfs(s)
        return mx
