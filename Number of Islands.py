"""
Number of Islands

We can delete each island using dfs as well.            
"""
class Solution:
    def solve(self, matrix):
        def remove_island(i,j):
            matrix[i][j]=0
            for di,dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj]:
                    remove_island(ni,nj)
        ans=0
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v: 
                    ans+=1
                    remove_island(i,j)
        return ans
