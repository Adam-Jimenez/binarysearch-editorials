"""
Flipped Matrix

Our first goal is to set all first bits to one using row flips, since they are the most significant.

Then, we iterate column by column, counting the total number of ones and zeroes. If there is a greater number of zeroes, we flip the whole column.
"""
class Solution:
    def solve(self, matrix):
        for r in matrix:
            if r[0]==0:
                for i in range(len(r)):
                    r[i] = -r[i]+1
        for j in range(1,len(matrix[0])):
            cnt=0
            for i in range(len(matrix)):
                cnt+=1 if matrix[i][j] else -1
            if cnt<0:
                for i in range(len(matrix)):
                    matrix[i][j] = -matrix[i][j]+1
        ans=0
        for r in matrix:
            a=0
            for v in r:
                a=2*a+v
            ans+=a
        return ans
