"""
Labyrinthian Possibilities

1D dp solution: we build upon the 2D DP solution described in my other editorial.

We noticed that for each row in our DP matrix, we copied the precedent row, so instead we can just re-iterate on the same row to avoid copying.
"""
class Solution:
    def solve(self, matrix):
        if matrix[0][0]: return 0
        matrix[-1][-1]=0
        dp = [0]*len(matrix[0])
        dp[0]=1 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]: dp[j] = 0
                elif j>0: dp[j] += dp[j-1]
        return dp[-1] % (10 ** 9 + 7)
