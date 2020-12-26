"""
Low Score

Basically Dijkstra's algorithm, but instead of using total distance as the min-heap key, we use the custom key described in the problem, the number of edges times the maximum weight.
"""
from collections import defaultdict,deque
from heapq import heappush, heappop
class Solution:
    def solve(self, edges):
        adj = defaultdict(list)
        nodes=set()
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            nodes.add(u)
            nodes.add(v)
        hp=[(0,0,0,0)]
        target = max(nodes)
        seen=set()
        while hp:
            key,edgecount,maxweight,cur = heappop(hp)
            if cur == target: 
                return key
            if cur in seen:
                continue
            seen.add(cur)
            for nei,wei in adj[cur]:
                next_edgecount = edgecount+1
                next_maxweight = max(maxweight, wei)
                next_key = next_edgecount*next_maxweight
                heappush(hp, (next_key, next_edgecount,next_maxweight, nei))
        return -1
        
