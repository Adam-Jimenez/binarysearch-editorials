"""
Sort String by Flipping

For every position in the string, compute the number of x's to the right and the number of y's to the left. The sum of those values equals the cost of changing the string to respect the constraint for the given split position. We return the minimum cost by checking every split position.
"""
class Solution:
    def solve(self, s):
        xr=[0 for _ in range(len(s)+1)]
        yl=[0 for _ in range(len(s)+1)]
        for i in range(len(s)-2, -2, -1):
            xr[i]=xr[i+1]+(s[i+1]=="x")
        for i in range(1,len(s)+1):
            yl[i]=yl[i-1]+(s[i-1]=="y")
        return min(x+y for x,y in zip(xr,yl))