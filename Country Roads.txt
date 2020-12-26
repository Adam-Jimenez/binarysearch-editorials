"""
Country Roads

Graph coloring solution. If we visualize our tree as rows of cities, we alternate between rows of town and rows of cities starting from the root. We chose the max out of the two possibilities.
"""
from collections import defaultdict
class Solution:
    def solve(self, source, dest, population):
        adj_list=defaultdict(list)
        color_cities=defaultdict(list)
        nodes=set()
        ends=set()
        for s,e in zip(source,dest):
            nodes.add(s)
            nodes.add(e)
            ends.add(e)
            adj_list[s].append(e)
        color=False
        start = (nodes-ends).pop()
        q=[start]
        while q:
            for _ in range(len(q)):
                cur=q.pop(0)
                color_cities[color].append(population[cur])
                for n in adj_list[cur]: q.append(n)
            color^=True
        return max(sum(x) for x in color_cities.values())
