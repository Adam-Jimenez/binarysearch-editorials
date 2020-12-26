"""
Length of Longest Balanced Subsequence

We can only take as many closing brackets as we have accumulated opening brackets, and the number of valid parentheses is denoted by the ones we have successfully closed, times two to take into account the opening brackets.
"""
class Solution:
    def solve(self, s):
        minn=maxx=0            
        for c in s:
            if c == "(": 
                maxx+=1
            elif minn<maxx: 
                minn+=1
        return 2*minn