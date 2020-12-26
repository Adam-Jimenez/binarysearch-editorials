"""
Longest Path in a Graph

The longest path starting from a node is the longest path starting from its neighbors plus one. In order to avoid recomputing the longest path starting from any node, we can memoize the result.
"""
from functools import lru_cache
class Solution:
    def solve(self, graph):
        @lru_cache(None)
        def dfs(i):
            if not graph[i]: return 0
            return max(dfs(j) for j in graph[i])+1
        return max(dfs(i) for i in range(len(graph)))
