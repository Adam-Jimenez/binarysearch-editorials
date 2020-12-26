"""
Square One

Similar idea to the Largest square medium problem, with the additional constraint that all values are equal. 

We create the additionnal dp matrix that stores the largest square with bottom-right corner at [i][j]. Then we iterate over the matrix: if a value is equal to its top, top-left and left values, then we can make a larger square with the smallest of its neighboring values.
"""
class Solution:
    def solve(self, matrix):
        dp =[[1]* len(matrix[0]) for _ in matrix]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == matrix[i-1][j-1] == matrix[i][j-1] == matrix[i-1][j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return max(v for r in dp for v in r)
