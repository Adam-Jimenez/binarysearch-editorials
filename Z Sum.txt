"""
Z Sum

We add the sum of the first row and the last row, plus the diagonal in between, making sure to not count the elements in the corner twice.

Edge cases are empty array and matrix of size 1x1.
"""
class Solution:
    def solve(self, matrix):
        if not matrix: return 0
        if len(matrix)==1: return matrix[0][0]
        return sum(matrix[0]) + sum(matrix[-1]) + \
        sum(matrix[i][~i] for i in range(1,len(matrix)-1))
