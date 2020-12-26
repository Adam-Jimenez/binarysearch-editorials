"""
Latin Square Solver

Similar to Sudoku Solver, we build a set of used numbers for each rows and each columns, then apply a backtracking approach to the empty cells, trying every possible value, and seeing if we can fill every square.
"""
class Solution:
    def solve(self, matrix):
        if not matrix: return True
        rows=[set() for _ in matrix]
        cols=[set() for _ in matrix[0]]
        empties=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]: return False
                    rows[i].add(matrix[i][j])
                    cols[j].add(matrix[i][j])
                else:
                    empties.append((i,j))
        def backtrack(x=0):
            if x == len(empties): return True
            i,j = empties[x]
            for val in range(1,len(matrix)+1):
                if val not in rows[i] and val not in cols[j]:
                    rows[i].add(val)
                    cols[j].add(val)
                    if backtrack(x+1): 
                        return True
                    cols[j].remove(val)
                    rows[i].remove(val)
            return False
        return backtrack()
