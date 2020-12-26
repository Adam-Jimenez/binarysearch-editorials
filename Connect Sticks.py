"""
Connect Sticks

We can treat this problem as a graph problem, where each endpoint is a node and each stick is an edge. We can only use each stick once, so we store the index of the stick in a set, and can only use sticks that aren't in this set.

The longest path problem is known to be NP-Hard:  https://en.wikipedia.org/wiki/Longest_path_problem. Therefore, we are forced to check all possible paths to find the longest one, making this solution exponential relative to the number of edges.

Not sure about time complexity, I think its O(a^n), where a is the average number of neighbors for each vertex and n is the maximum length of each path, which is the number of endpoints.

O(n) space complexity, for storing graph and seen sticks.
"""
from collections import defaultdict

class Solution:
    def solve(self, sticks):
        adj=defaultdict(set)
        endpoint={end for stick in sticks for end in stick}
        for i,(s,e) in enumerate(sticks):
            adj[s].add((i,e))
            adj[e].add((i,s))
            
        def dfs(end,seen=set()):
            return max(1+dfs(nei, seen|{i}) if i not in seen else 0 for i,nei in adj[end])
        return max(dfs(end) for end in endpoint)
