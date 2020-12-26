"""
Wildfire

Some people just want to see the world burn... https://www.youtube.com/watch?v=6l6vqPUM_FE
"""
from collections import deque
class Solution:
    def solve(self, matrix):
        if not matrix: return 0
        q=deque([(i,j) for i,r in enumerate(matrix) for j,v in enumerate(r) if v==2])
        ans=0
        while q:
            burned=False
            for _ in range(len(q)):
                i,j=q.popleft()
                neighbors=[]
                for di,dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                    ni,nj=i+di,j+dj
                    if ni>=0 and nj>=0 and ni<len(matrix) and nj<len(matrix[0]) and matrix[ni][nj]==1:
                        burned=True
                        matrix[ni][nj]=2
                        q.append((ni,nj))
            ans+=int(burned)
        return ans if all(all(x!=1 for x in r) for r in matrix) else -1
    