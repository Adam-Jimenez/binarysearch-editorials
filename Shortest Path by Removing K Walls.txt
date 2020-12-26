"""
Shortest Path by Removing K Walls

This is like a regular BFS, with the twist being with how we handle our seen set.

Instead of just storing seen coordinates in a set, we now store the number of walls left when we reached that position. Knowing that when we BFS, the minimal cost path will be explored first, the only way to find a more optimal path when re-exploring a same path is to have more wall removals in reserve. 
"""
from collections import deque
class Solution:
    def solve(self, matrix, k):
        def adj(i,j):
            for ni,nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]):
                    yield ni,nj
        seen={}
        seen[(0,0)]=0
        q=deque([(0,0,0,0)]) # (cost,walls, i,j)
        while q:
            cost,wall_removed,i,j = q.popleft()
            if i == len(matrix)-1 and j == len(matrix[0])-1:
                return cost
            for ni,nj in adj(i,j):
                new_wall = wall_removed+matrix[ni][nj]
                if new_wall>k: 
                    continue
                if (ni,nj) in seen and seen[(ni,nj)]<=new_wall:
                    continue
                seen[(ni,nj)]=new_wall
                nxt=(cost+1, new_wall,ni,nj)
                q.append(nxt)
        return -1