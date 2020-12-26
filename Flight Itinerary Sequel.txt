"""
Flight Itinerary Sequel

This problem consists in finding an Eulerian path (or circuit) in a graph. An Eulerian path is a path that passes through all the edges of a graph, and in this problem the edges are represented by flights.

The algorithm implemented here is Hierholzer's algorithm, the fastest algorithm that i know of. It runs in O(|E|), |E| being the number of edges. This video explains it in detail: https://www.youtube.com/watch?v=8MpoO2zA2l4.


"""
from collections import defaultdict
class Solution:
    def solve(self, flights):
        ins = defaultdict(int)
        outs = defaultdict(int)
        adj_list = defaultdict(list)
        for s,e in flights:
            adj_list[s].append(e)
            outs[s]+=1
            ins[e]+=1
        for l in adj_list.values():
            l.sort()
        start=None
        end=None
        for airport in adj_list.keys():
            if outs[airport]-ins[airport] == 1:
                if start:  return
                start = airport
            elif outs[airport]-ins[airport] == -1:
                if end: return
                end = airport
            elif outs[airport]-ins[airport] != 0: return
        start=start if start else min(adj_list.keys())
        ans=[]
        def dfs(airport):
            while outs[airport]:
                nxt=len(adj_list[airport])-outs[airport]
                outs[airport]-=1
                dfs(adj_list[airport][nxt])
            ans.append(airport)
        dfs(start)
        return ans[::-1]