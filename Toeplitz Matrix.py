"""
Toeplitz Matrix

You don't need to iterate each diagonal individually. Checking equality with the direct diagonal neighbor is enough.

"""
class Solution:
    def solve(self, matrix):
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if (matrix[i][j] != matrix[i+1][j+1]):
                    return False
        return True
        # Write your code here
