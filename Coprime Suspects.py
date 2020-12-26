"""
Coprime Suspects

BFS approach. I hate math so i just let computers try all possibilities for me.
"""
from math import gcd
class Solution:
    def solve(self, a, b):
        def bfs(a,b):
            dist={(a,b):0}
            q=[(a,b)]
            while True:
                ca,cb = q.pop(0)
                cost=dist[(ca,cb)]
                if gcd(ca,cb) != 1: return cost
                for da, db in [(-1,0),(0,-1),(1,0),(0,1)]:
                    na,nb = ca+da, cb+db
                    if (na,nb) not in dist:
                        dist[(na,nb)]=cost+1
                        q.append((na,nb))
        return bfs(a,b)