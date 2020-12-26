"""
Longest Common Substring

Check if ith character in one string A is equal to jth character in string B

Case 1: both characters are same

LCS[i][j] = 1 + LCS[i-1][j-1] (add 1 to the result and remove the last character from both the strings and check the result for the smaller string.)

Case 2: both characters are not same.

LCS[i][j] = 0

At the end, traverse the matrix and find the maximum element in it, This will the length of Longest Common Substring.

https://algorithms.tutorialhorizon.com/dynamic-programming-longest-common-substring/
"""
class Solution:
    def solve(self, s0, s1):
        dp=[[0 for _ in s1] for _ in s0]
        for i in range(len(s1)):
            dp[0][i] = s1[i]==s0[0]
        for i in range(len(s0)):
            dp[i][0] = s0[i]==s1[0]
        for i in range(1,len(s0)):
            for j in range(1,len(s1)):
                if s0[i]==s1[j]:
                    dp[i][j] = 1+dp[i-1][j-1]
        return max(max(r) for r in dp)