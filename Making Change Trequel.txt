"""
Making Change Trequel

2D dp solution: each row represent the coin currently being tested, each col represents the current amount. Best learned by watching videos on the problem.

Here's my attempt at a video explanation: https://www.youtube.com/watch?v=bV1CvGRu4cg&t=56s
"""
class Solution:
    def solve(self, denominations, amount):
        dp = [[0]*(amount+1) for _ in denominations]
        for i in range(len(denominations)):
            dp[i][0]=1
        for k in range(1,amount+1):
            for i,d in enumerate(denominations):
                if i > 0: dp[i][k] = dp[i-1][k]
                if k-d >= 0: dp[i][k] += dp[i][k-d]
        return dp[-1][-1] % (10 ** 9 + 7)
                
