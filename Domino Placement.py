"""
Domino Placement

If we fill the board with vertical dominos, we can fit n dominos in width and m//2 dominos in height. If the height is uneven, we have to put dominos sideways on the last row, so we divide the width by two.
"""
class Solution:
    def solve(self, n, m):
        return (n*(m-(m&1))//2)+(m&1)*n//2
