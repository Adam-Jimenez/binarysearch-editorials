"""
Matrix Rectangular Sums

The key to this problem is to compute 2D prefix sum. To compute the prefix sum from coordinates (0,0) to (i,j), in O(n^2), we can use the following recurrence relation: 

`prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]`

The sum of the rectangle is the sum of the rectangle above it and to the left of it, minus the overlapping part. It helps to use a defaultdict to avoid handling edges cases with out of bound coordinates. 

Then, using the prefix sum, we can cut out the sum of a square section of the matrix in constant time by taking the prefix sum to the bottom left coordinate of the square, removing everything to the left and above of the square, and re-adding the part we subtracted twice, following the inclusion-exclusion principle. 
"""
from collections import defaultdict
class Solution:
    def solve(self, matrix, k):
        pre=defaultdict(int)
        R,C = len(matrix), len(matrix[0])
        for i in range(R+k):
            for j in range(C+k):
                pre[(i,j)] = pre[(i-1,j)] \
                + pre[(i,j-1)] \
                - pre[(i-1,j-1)]
                if i<len(matrix) and j < len(matrix[0]):
                    pre[(i,j)] += matrix[i][j]
        return [[
                pre[(i+k, j+k)] \
                + pre[(i-k-1, j-k-1)] \
                - pre[(i+k, j-k-1)] \
                - pre[(i-k-1, j+k)]
                for j in range(C)
            ] for i in range(R)]
                