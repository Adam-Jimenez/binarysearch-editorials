"""
Knight Remains

Since each move is equiprobable, the probability of staying in the board for a cell is the sum of the probabilities of the cells you can jump to divided by 8. We recurse to a depth of k.
"""
from functools import lru_cache
moves=[(1,2),(1,-2), (-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
class Solution:
    def solve(self, n, x, y, k):
        @lru_cache(None)
        def dfs(x,y,k):
            if x<0 or y <0 or x>=n or y>=n: return 0
            if k == 0: return 1
            return sum(dfs(x+dx, y+dy,k-1)/8 for dx,dy in moves)
        return int(dfs(x,y,k)*100)
