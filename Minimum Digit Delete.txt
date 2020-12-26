"""
Minimum Digit Delete

Algorithm based on Levenshtein distance, where the cost of deleting a character is the value of the digit deleted.

https://en.wikipedia.org/wiki/Levenshtein_distance
"""
class Solution:
    def solve(self, s0, s1):
        dp=[[0 for _ in range(len(s1)+1)] for _ in range(len(s0)+1)]
        for i in range(1,len(s0)+1):
            dp[i][0]=dp[i-1][0]+int(s0[i-1])
        for j in range(1,len(s1)+1):
            dp[0][j]=dp[0][j-1]+int(s1[j-1])
        for i in range(1,len(s0)+1):
            for j in range(1,len(s1)+1):
                dp[i][j] = min(
                    dp[i-1][j]+int(s0[i-1]),
                    dp[i][j-1]+int(s1[j-1])
                    )
                if s0[i-1]==s1[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        return dp[-1][-1]