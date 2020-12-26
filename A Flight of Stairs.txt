"""
A Flight of Stairs

Classic DP problem, identical to fibonacci. https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
"""
MOD=(10**9)+7
class Solution:
    def solve(self, n):
        dp=[0 for _ in range(n+2)]
        dp[1]=1
        for i in range(2,n+2):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]%MOD