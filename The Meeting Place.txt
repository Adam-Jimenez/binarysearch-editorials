"""
The Meeting Place

For each twos (2) in the grid, we create a cost matrix using BFS.

Then we iterate over each index, calculating the sum of the cost matrix of every two and taking the min from all the sums.
"""
class Solution:
    def solve(self, matrix):
        twos={}
        costs={}
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v==2:
                    twos[(i,j)]=[(i,j,0)]
                    costs[(i,j)]=[[1e9 for _ in matrix[0]] for _ in matrix]
        for k,q in twos.items():
            seen=set()
            while q:
                i,j,cost=q.pop(0)
                if (i,j) in seen: continue
                seen.add((i,j))
                costs[k][i][j] = cost
                for di, dj in ((1,0),(-1,0), (0,1),(0,-1)):
                    ni,nj=i+di,j+dj
                    if ni>=0 and nj>=0 and ni<len(matrix) and nj<len(matrix[0]) and matrix[ni][nj]!=1:
                        q.append((ni,nj,cost+1))
        ans=1e9
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur_cost=0
                for arr in costs.values():
                    cur_cost+=arr[i][j]
                ans=min(ans,cur_cost)
        return ans
