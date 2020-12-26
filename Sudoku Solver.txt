"""
Sudoku Solver

Simple backtracking solution, with the only optimization being storing taken values in a set, to be able to get all possible values without iterating through the grid.
"""
class Solution:
    def solve(self, matrix):
        # taken values for each set
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        regions=[set() for _ in range(9)]
        
        # all possible values for a set
        nums=set(range(1,10))
        
        # populate sets
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    rows[i].add(matrix[i][j])
                    cols[j].add(matrix[i][j])
                    regions[get_region(i,j)].add(matrix[i][j])
                    
        # backtrack on all possible values
        def backtrack(i=0,j=0):
            if i>=9: return True
            if matrix[i][j]:
                i,j = it(i,j)
                return backtrack(i,j)
            possibilities = nums - rows[i] - cols[j] - regions[get_region(i,j)]
            for num in possibilities:
                rows[i].add(num)
                cols[j].add(num)
                regions[get_region(i,j)].add(num)
                matrix[i][j]=num
                if backtrack(*it(i,j)): return True
                matrix[i][j]=0
                rows[i].remove(num)
                cols[j].remove(num)
                regions[get_region(i,j)].remove(num)
            return False
            
        if backtrack(): return matrix
        return False
        
# helper functions
def it(i,j):
    j+=1
    i+=j//9
    j%=9
    return i,j
    
def get_region(i,j):
    return i-i%3 + j//3
