"""
Shortest Bridge

We iterate over the array to find the first one we see, record its position. Then, we do BFS to find the border of the first island. Finally, we do BFS using the border of the first island to count the number of steps we need to reach the border of the second island.
"""
from collections import deque
class Solution:
    def solve(self, arr):
        def get_neighbors(i,j):
            for di,dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni,nj = i+di, j+dj
                if ni>=0 and nj>=0 and ni<len(arr) and nj<len(arr[0]):
                    yield ni,nj
                    
        start=None
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 1:
                    start=(i,j)
                    break
        q=deque([start])
        seen=set()
        nseen=set()
        while q:
            i,j = q.popleft()
            if (i,j) in seen: continue
            seen.add((i,j))
            for ni,nj in get_neighbors(i,j):
                if arr[ni][nj] == 0: 
                    nseen.add((i,j))
                else:
                    q.append((ni,nj))
                    
        nq = deque(nseen)
        ans=0
        while nq:
            for _ in range(len(nq)):
                i,j = nq.popleft()
                if ans>0 and arr[i][j] == 1: return ans-1
                for ni,nj in get_neighbors(i,j):
                    if (ni,nj) in seen: continue
                    seen.add((ni,nj))
                    nq.append((ni,nj))
            ans+=1