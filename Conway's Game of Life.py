"""
Conway's Game of Life

This solution focuses on simplicity and not performance. 

Using an in_bounds function can be useful if you want to iterate over the neighbors without worrying about being outside the matrix.
"""
class Solution:
    def solve(self, matrix):
        next=[[0]*len(matrix[0]) for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                neighbor_cnt = 0
                for n1 in range(i-1, i+2):
                    for n2 in range(j-1, j+2):
                        if (n1 != i or n2 != j) and in_bounds(n1,n2, matrix):
                            neighbor_cnt += matrix[n1][n2]
                if matrix[i][j]==1 and neighbor_cnt in [2,3]:
                    next[i][j]=1
                elif matrix[i][j]==0 and neighbor_cnt == 3:
                    next[i][j]=1
        return next
                
def in_bounds(i,j, matrix):
    return i>=0 and j>=0 and i<len(matrix) and j<len(matrix[0])