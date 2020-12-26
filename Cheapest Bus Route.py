"""
Cheapest Bus Route

We can use dijkstra's algorithm, with the nuance in how we handle our seen nodes. We need to keep track of which bus we were on when we visited a node, as results may vary depending on that.
"""
from heapq import heapify, heappop, heappush
from collections import defaultdict
class Solution:
    def solve(self, connections):
        start = 0
        target = max(max(y,x) for y,x,_ in connections)
        
        adj = defaultdict(list)
        for f,t,id in connections:
            adj[f].append((t,id))
            
        hp = [(0, start, -1)] # (cost, cur_pos cur_bus)
        seen = defaultdict(set)
        
        while hp:
            cost, cur_pos, cur_bus = heappop(hp)
            if cur_pos == target:
                return cost
            if cur_bus in seen[cur_pos]:
                continue
            seen[cur_pos].add(cur_bus)
                
            for nex_pos, nex_bus in adj[cur_pos]:
                next_cost = cost
                if nex_bus != cur_bus:
                    next_cost += 1
                heappush(hp, (next_cost, nex_pos, nex_bus))
            
        return -1