"""
Flip and Invert Matrix

We can do both operations at the same time in a list comprehension, iterating over rows, and flipping the corresponding value from the end of the row.
"""
class Solution:
    def solve(self, matrix):
        return [[1^row[~j] for j in range(len(row))] for row in matrix]
