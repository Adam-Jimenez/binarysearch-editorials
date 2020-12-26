"""
Minimum Number of Operations to Make Lists Increasing

DP solution, where the tracked state is the position and whether we swapped the previous items:
We try the sub problem where we don't swap (if it respects the constraints of the problem - a[i]>a[i-1] and b[i]>b[i-1]),
and the sub problem where we swap (again, if it respects the constraints).

We take the minimum output from both sub problems.

O(n) time, O(n) space
"""
from functools import lru_cache
class Solution:
    def solve(self, a, b):
        @lru_cache(None)
        def dp(i=0,prevswapped=False):
            if len(a)==i:
                return 0
            elif i == 0:
                # We are free to do whatever on first index
                return min(dp(i+1), 1+dp(i+1,True))
            else:
                preva=a[i-1]
                prevb=b[i-1]
                if prevswapped:
                    preva,prevb=prevb,preva
                # forced to swap, otherwise constraints are not respect
                if a[i]<=preva or b[i]<=prevb: 
                    return 1+dp(i+1,True)
                else:
                    # Try not swapping
                    ans=dp(i+1)
                    # If constraints are still respected, try swapping
                    if a[i]>prevb and b[i]>preva:
                        ans=min(ans,1+dp(i+1,True))
                    return ans
        return dp()