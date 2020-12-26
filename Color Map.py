"""
Color Map

We find groups of different colors using BFS, and storing the count of groups of a certain color in a dictionary.

Then, we want to keep the most frequent color, and change the rest of the groups that aren't of that color.
"""
from collections import defaultdict,deque
class Solution:
    def solve(self, matrix):
        if not matrix: return 0
        def get_neighbors(i,j):
            for di,dj in [(-1,0), (1,0), (0,1), (0,-1)]:
                ni,nj = i+di, j+dj
                if ni>=0 and nj>=0 and ni<len(matrix) and nj<len(matrix[0]):
                    yield (ni,nj)
                    
        colors=defaultdict(int)
        seen=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i,j) not in seen:
                    ref_color = matrix[i][j]
                    colors[ref_color]+=1
                    q=deque([(i,j)])
                    while q:
                        cur=q.popleft()
                        ci,cj=cur
                        if matrix[ci][cj] != ref_color or cur in seen: continue
                        seen.add(cur)
                        for ni,nj in get_neighbors(ci,cj):
                            q.append((ni,nj))
        freq=sorted(list(colors.values()))
        mx = freq.pop()
        return sum(freq)