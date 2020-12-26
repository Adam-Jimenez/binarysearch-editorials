"""
N Queens Puzzle

Other solutions are pretty clever, but for completeness' sake, here's a backtracking implementation that solves the problem.
"""
class Solution:
    def solve(self, matrix):
        self.matrix=matrix
        self.N = len(matrix)
        self.rows=set()
        self.cols=set()
        self.diags=set()
        self.backdiags=set()
        for i,r in enumerate(matrix):
            for j,v in enumerate(r):
                if v:
                    if not self.add_pos(i,j):
                        return False
        return self.backtrack()
        
    def pos_unused(self,i,j):
        return all((
            i not in self.rows,
            j not in self.cols,
            (j-i) not in self.diags,
            (j+i) not in self.backdiags
        ))
        
    def add_pos(self,i,j):
        if not self.pos_unused(i,j): 
            return False
        self.rows.add(i)
        self.cols.add(j)
        self.diags.add(j-i)
        self.backdiags.add(j+i)
        return True
        
    def remove_pos(self,i,j):
        self.rows.remove(i)
        self.cols.remove(j)
        self.diags.remove(j-i)
        self.backdiags.remove(j+i)
        
    def seek(self,i=0,j=0):
        while i<self.N:
            if self.pos_unused(i,j):
                yield i,j
            j+=1
            i+=j//self.N
            j=j%self.N
        
    def done(self):
        return len(self.rows)==self.N
        
    def backtrack(self,i=0,j=0):
        if self.done():  return True
        for i,j in self.seek(i,j):
            self.add_pos(i,j)
            if self.backtrack(i+1,0): return True
            self.remove_pos(i,j)
        return False
    
