"""
Distinct Islands

For every piece of land found, I apply BFS, and add every position of land relative to the first piece of land in a set. 

I convert it to a frozen set, a immutable set, so that we can put the set into sets. The length of the set of islands is our answer.

O(N) time, O(N) space, where N is number of tiles.
"""
from collections import deque
class Solution:
    def solve(self, matrix):
        def get_neighbors(i,j):
            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if ni>=0 and nj>=0 and ni<len(matrix) and nj<len(matrix[0]) and matrix[ni][nj]:
                    yield ni,nj
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            rel=set()
            matrix[i][j]=0
            while q:
                ci, cj= q.popleft()
                rel.add((ci-i,cj-j))
                for ni,nj in get_neighbors(ci,cj):
                    matrix[ni][nj]=0
                    q.append((ni,nj))
            return frozenset(rel)
        islands=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    islands.add(bfs(i,j))
        return len(islands)
                    
