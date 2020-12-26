"""
Knights' Attack

We iterate over the matrix and for each knight we find, we try all his possible moves and check if a knight is there.
"""
class Solution:
    def solve(self, matrix):
        moves=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    for di,dj in moves:
                        if check(i+di,j+dj,matrix): return True
        return False
                
def check(i,j,matrix):
    return i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0]) and matrix[i][j]
