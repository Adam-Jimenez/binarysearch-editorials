"""
Distributed Systems

Dijkstra's algorithm for shortest path in a graph. Similar to BFS, but we use a min-heap that uses the cost as the key, so we greedily process the lowest cost node at any time.
"""
from heapq import heappush, heappop
class Solution:
    def solve(self, n, edges):
        adj_list=[[] for _ in range(n+1)]
        for start,end,cost in edges:
            adj_list[start].append((cost,end))
            adj_list[end].append((cost,start))
        q=[(0,0)]
        seen=[False for _ in range(n+1)]
        mcost=0
        while q:
            cost,node=heappop(q)
            if seen[node]: continue
            seen[node]=True
            mcost=max(mcost,cost)
            for ncost, nnode in adj_list[node]:
                heappush(q,(cost+ncost, nnode))
        return mcost
