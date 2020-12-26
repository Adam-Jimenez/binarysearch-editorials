"""
Bomber Man Sequel

O(N*M):

I stored the enemies you could reach in the current row from any position, and the enemies you could reach in the current column from any position,  then I summed the results from both matrices and returned the max answer.

To avoid re-iterating over the same squares in the same row/col, I emulated an int pointer using a single-position array. While iterating over a row col, I assigned the current pointer to the position, and each time that I met an enemy, I incremented that same pointer. Each time I met a wall, I no longer wanted to modify the previous position, so I reinitialized a new pointer for the future cells.
"""
class Solution:
    def solve(self, matrix):
        rows={}
        cols={}
        for i in range(len(matrix)):
            cur=[0]
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2:
                    cur[0]+=1
                elif matrix[i][j] == 1:
                    cur=[0]
                rows[(i,j)]=cur
        for j in range(len(matrix[0])):
            cur=[0]
            for i in range(len(matrix)):
                if matrix[i][j] == 2:
                    cur[0]+=1
                elif matrix[i][j] == 1:
                    cur=[0]
                cols[(i,j)]=cur
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    count=rows[(i,j)][0]+cols[(i,j)][0]
                    ans=max(ans,count)
        return ans
