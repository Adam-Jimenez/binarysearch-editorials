"""
Corner Diagonals

If n is even, diagonals don't intersect and they each contain n cells, so we remove from the total number of cells (n*n) the diagonals (2*n).

If n is odd, the diagonals intersect in the center, so in order to not double-count it, we add back one, which gives n*n - 2*n + 1
"""
class Solution:
    def solve(self, n):
        return n*n-2*n+1 if n&1 else n*n-2*n
