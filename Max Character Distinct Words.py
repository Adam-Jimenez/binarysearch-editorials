"""
Max Character Distinct Words

O(N^3) solution. (set intersection is linear)

We check each pair, check that the intersection of the sets of letters is empty, if so we save the max length.
"""
class Solution:
    def solve(self, words):
        ltrs={w:set(w) for w in words}
        mx=0
        for i in range(len(words)):
            w1=words[i]
            for j in range(i+1, len(words)):
                w2=words[j]
                if len(ltrs[w1]&ltrs[w2])==0:
                    mx=max(mx, len(w1)+len(w2))
        return mx
