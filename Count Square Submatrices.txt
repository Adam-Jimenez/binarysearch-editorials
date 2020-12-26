"""
Count Square Submatrices

To make a 2x2 square from a 1x1 square, each of its top, left and top-left neighbors must be one:
1 1
1 2
This extends to squares of any dimensions - it is always constraint by the smallest neighbor:
1 2
2 2
Will also give give a square of 2x2, we are missing the top-left cell to make a 3x3.

We can take the min of those three neighbors + 1, get the number of square this cell belongs to, and finally add that number to our answer.
"""
class Solution:
    def solve(self, matrix):
        ans=0
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v:
                    if i>0 and j>0:
                        matrix[i][j] += min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
                    ans += matrix[i][j]
        return ans
