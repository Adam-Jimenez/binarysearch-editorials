"""
Largest Square Submatrix

Every square of side n is formed of three overlapping square of side (n-1). The subsquare's position are at i,j-1 i-1,j and i-1,j-1. The bigger square can only be as big as the smallest subsquare, plus one.
"""
class Solution:
    def solve(self, matrix):
        a=0
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v: a=max(a,1)
                if i==0 or j==0 or v==0: continue
                matrix[i][j]=min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])+1
                a=max(a,matrix[i][j])
        return a**2