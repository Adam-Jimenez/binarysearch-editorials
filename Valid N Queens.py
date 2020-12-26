"""
Valid N Queens

We can validate each of the three constraints to this problem in one line each.

To validate that there is exactly one queen per row, we return False if any row contains more (or less) than one queen.
To validate that there is exactly one queen per column, we repeat the same process as above on the tranposed matrix.
To validate that there is only one queen per diagonal, we can use a cool trick. For each unique diagonal in a grid, the value of j-i will be constant, because when we iterate over a diagonal, we add one to both j and i.
Here's an example of grid[i][j] = j-i:
```
i/j 0  1  2
 0  0  1  2
 1 -1  0  1
 2 -2 -1  0
```
So we can create a set of all unique (j-i) values and check that it equals the number of required queens, N (the length of the matrix).

To check for backward diagonals, we can do the same process with (i+j):
```
i/j 0  1  2
 0  0  1  2
 1  1  2  3
 2  2  3  4
```
"""
class Solution:
    def solve(self, matrix):
        if any(row.count(1) != 1 for row in matrix): return False
        if any(col.count(1) != 1 for col in zip(*matrix)): return False
        if len(set(j-i for i,row in enumerate(matrix) for j,queen in enumerate(row) if queen)) != len(matrix): return False
        return len(set(j+i for i,row in enumerate(matrix) for j,queen in enumerate(row) if queen)) == len(matrix)
