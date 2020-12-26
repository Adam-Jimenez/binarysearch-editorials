"""
Painting Houses

For each cell in a row, we take the minimum value from the previous row excluding the current column and add it to the current cell. 

If we do that naively, we will timeout, so one trick we can do is only keep the two minimum values - taking the second value if the column of the smallest value is the same as the current cell, otherwise taking the smallest value.
"""
class Solution:
    def solve(self, matrix):
        a,b=1e9,1e9
        ia,ib=-1,-1
        for i in range(len(matrix[0])):
            n = matrix[0][i]
            if n < a: 
                a,b = n,a
                ia,ib = i,ia
            elif n<b: 
                b=n
                ib=i
        for i in range(1,len(matrix)):
            cura,curb=1e9, 1e9
            curia, curib=-1,-1
            for j in range(len(matrix[0])):
                mn=a if j != ia else b
                matrix[i][j] += mn
                v = matrix[i][j]
                if v < cura:
                    cura, curb = v, cura
                    curia, curib = j, curia
                elif v < curb:
                    curb = v
                    curib = j
            a,b=cura,curb
            ia,ib = curia,curib
        return a
