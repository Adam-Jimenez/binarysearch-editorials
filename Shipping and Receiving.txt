"""
Shipping and Receiving

Inspired by alex's answer.
We compute the shortest path starting from every node __once__, then query the correct dictionary.
"""
from functools import lru_cache
class Solution:
    def solve(self, ports, shipments):
        @lru_cache(None)
        def bfs(source):
            dist = {source: 0}
            queue = [source]
            for node in queue:
                for nei in ports[node]:
                    if nei not in dist:
                        dist[nei] = dist[node] + 1
                        queue.append(nei)
            return dist
        
        return sum(bfs(u).get(v, 0) for u, v in shipments)

