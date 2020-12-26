"""
Big Numbers

We calculate the max of each row and of each column, and check if both are equal to the cell for any position.

zip(*matrix) is a cool trick that will transpose your matrix.
"""
class Solution:
    def solve(self, matrix):
        transpose = zip(*matrix)
        maxr = [max(row) for row in matrix]
        maxc = [max(col) for col in transpose]
        return sum(matrix[i][j] == maxr[i] == maxc[j] 
                for j in range(len(matrix[0]))
                for i in range(len(matrix))
            )
