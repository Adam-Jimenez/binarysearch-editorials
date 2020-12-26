"""
Bomber Man

Same logic as alex's answer, but shorter. The number of safe cells is the product of the number of safe rows times the number of safe columns.
"""
class Solution:
    def solve(self, matrix):
        rows=sum(1 for r in matrix if 1 not in r)
        cols=sum(1 for c in zip(*matrix) if 1 not in c)
        return rows*cols
