"""
The Maze Runner

We can count the number of layers the BFS has to explore to reach its target by adding a for loop, exploring only the current nodes in the queue.
"""
from collections import deque
class Solution:
    def solve(self, matrix):
        if matrix[0][0]: return -1
        w,h=len(matrix[0]),len(matrix)
        s,e=(0,0),(h-1,w-1)
        q=deque([s])
        seen=set()
        ans=1
        while q:
            for _ in range(len(q)):
                pos=q.popleft()
                if pos==e: return ans
                if pos in seen: continue
                seen.add(pos)
                i,j=pos
                for ni,nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                    if 0<=ni<h and 0<=nj<w and matrix[ni][nj]==0:
                        q.append((ni,nj))
            ans+=1
        return -1
