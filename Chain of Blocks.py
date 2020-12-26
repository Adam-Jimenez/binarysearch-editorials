"""
Chain of Blocks

Memoized solution: we store starts into a dictionary and then check max length path.
"""
from collections import defaultdict
from functools import lru_cache
class Solution:
    def solve(self, blocks):
        if not blocks: return 0
        starts=defaultdict(list)
        for s,e in blocks:
            starts[s].append(e)
        @lru_cache(None)
        def dfs(cur):
            ans=1
            for end in starts[cur]:
                if end in starts:
                    ans=max(ans, dfs(end)+1)
            return ans
        return max(dfs(i) for i in starts.keys())