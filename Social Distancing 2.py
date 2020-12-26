"""
Social Distancing 2

Dynamic programming isn't that hard, right guys? (right?). 
"""
class Solution:
    def solve(self, matrix):
        dp=[[0]*len(matrix[0]) for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]: continue
                if i>0: dp[i][j] = dp[i-1][j]+1
                if j>0: dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
                if i>0 and j>0: dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
                if i>0 and j<len(matrix[0])-1: dp[i][j] = min(dp[i][j], dp[i-1][j+1]+1)
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j]: continue
                if j<len(matrix[0])-1: dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
                
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j]: continue
                if i<len(matrix)-1: dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                if j<len(matrix[0])-1: dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
                if i<len(matrix)-1 and j<len(matrix[0])-1: dp[i][j] = min(dp[i][j], dp[i+1][j+1]+1)
                if j>0 and i<len(matrix)-1: dp[i][j] = min(dp[i][j], dp[i+1][j-1]+1)
            for j in range(len(matrix[0])):
                if matrix[i][j]: continue
                if j>0: dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        return max(v for r in dp for v in r)
                
