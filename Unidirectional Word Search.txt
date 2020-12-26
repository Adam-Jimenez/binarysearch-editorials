"""
Unidirectional Word Search

For every position, we iterate in both directions while the characters from the word and the board match. If we reach the end of the word, we have found it.
"""
class Solution:
    def solve(self, board, word):
        def dfs(i,j,k,right):
            if k>=len(word): return True
            if i<0 or i>= len(board) or j<0 or j>=len(board[0]) or \
                board[i][j] != word[k]: return False
            if right and dfs(i,j+1,k+1,right): return True
            if not right and dfs(i+1,j,k+1,right): return True
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0,True): return True
                if dfs(i,j,0,False): return True
        return False
            
