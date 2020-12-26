"""
Popularity

The number of paths going through (a,b) is the number of children nodes counting from b (e) times the rest of the nodes.

Explained in detail in this video (I made :D): https://www.youtube.com/watch?v=6s0ZRkJDeRc
"""
from collections import defaultdict
from functools import lru_cache
class Solution:
    def solve(self, edges):
        adj=defaultdict(list)
        node_count=len({node for edge in edges for node in edge})
        ans=[]
        for s,e in edges: adj[s].append(e)
        @lru_cache(None)
        def children_count(node):
            return sum(children_count(nei)+1 for nei in adj[node])
        for s,e in edges:
            ends=children_count(e)+1
            starts = node_count-ends
            ans.append(starts*ends)
        return ans