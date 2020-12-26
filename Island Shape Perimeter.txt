"""
Island Shape Perimeter

Every one in the matrix adds 4 to the perimeter, unless it has neighbors. In that case, it contributes 4 minus the number of neighbors.
"""
class Solution:
    def solve(self, matrix):
        def get(i,j):
            if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]):
                return 0
            return matrix[i][j]
        ans=0
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v==1:
                    p=4
                    for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                        if get(ni,nj): p-=1
                    ans+=p
        return ans
                    
