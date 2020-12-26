"""
Longest Concatenated String

We can solve the problem in linear time by iterating through the words backwards, and adding them in buckets based on their first letter.
When we reach a word, we check in the bucket corresponding to its last letter, and store the number of words at that moment in the bucket. This way, if we add words that are before the word in the list, they will not be considered.

Then, we can apply a DP algorithm on the graph. For each word i, we look at the longest concatenation we can make from its children, where the last character is equal to the first one. We don't have to worry about cycles, since we know that only words coming after the current one are neighbors.

O(n) time, but with a high coefficient, because the first letter than can 26 values.
O(n) space
"""
from collections import defaultdict
from functools import lru_cache
class Solution:
    def solve(self, words):
        adj=defaultdict(int)
        ltrs=defaultdict(list)
        for i in range(len(words)-1,-1,-1):
            cur=words[i]
            last=cur[-1]
            adj[i]=len(ltrs[last])
            ltrs[cur[0]].append(i)
                
        @lru_cache(None)
        def dp(i, first):
            cur=words[i]
            ans=float("-inf")
            if cur[-1]==first:
                ans=len(cur)
            last=cur[-1]
            for nei in range(adj[i]):
                ans=max(ans, len(cur)+dp(ltrs[last][nei],first))
            return ans
        return max(0,max(dp(i,words[i][0]) for i in range(len(words))))