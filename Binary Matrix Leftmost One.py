"""
Binary Matrix Leftmost One

For each row, we binary search for the leftmost occurence of a 1. We take the minimum answer, or return -1 if no answer is found.

O(R*log(C)) time
O(1) space
"""
from bisect import bisect_left
INF=float('inf')
class Solution:
    def solve(self, matrix):
        ans=INF
        for r in matrix:
            i=bisect_left(r,1)
            if i <len(r):
                ans=min(ans,i)
        return ans if ans < INF else -1
