"""
Condo Developers

We compute the max for each rows and each columns. zip(*matrix) is the matrix transposed, where each row are the columns.

Since we can't change the maximum of any row or column, we must be equal to the minimum of the max of the row and the max of the column we are modifying.
"""
class Solution:
    def solve(self, matrix):
        rows=[max(r) for r in matrix]
        cols=[max(c) for c in zip(*matrix)]
        ans=[[0 for _ in r] for r in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[i][j] = min(rows[i], cols[j])
        return ans
